
# Blockchain/EVM - The Basics

Point count: 368

Provided files: `evm.txt`

**Description:**

I have some EVM runtime bytecode, whatever that means. You need to find the value, in hex, that you need to send to make the contract STOP and not self destruct. Wrap the hex in n00bz{}. If the correct answer is 9999, the flag is n00bz{0x270f}. Author: NoobMaster

# Solution

**Solver:** lolmenow
First we find out what EVM runtime bytecode is, after some googling, we find that it is the result after you compile a smart contract, it tells the host what to do with the data it gets from the user. Runtime bytecode in particular, opposed to creation bytecode tells the host how to run the program, not how to initialize it.

Ok, now that we know what EVM bytecode is, we need to find a way to understand it, to do this we can use a decompiler like the following
[app.dedaub.com/decompile](https://app.dedaub.com/decompile)

that gets us the following bytecode:
```
    0x0: PUSH0     
    0x1: CALLVALUE 
    0x2: PUSH2     0x1337
    0x5: MUL       
    0x6: PUSH6     0xfdc29ff358a3
    0xd: EQ        
    0xe: PUSH1     0x12
   0x10: JUMPI     
   0x11: SELFDESTRUCT
   0x12: STOP      
```

to understand this we can find some documentation, [www.ethervm.io/](https://www.ethervm.io/#opcodes), which lists all of the 

ok now for a quick explanation line by line
 - 0x0: PUSH0 - this, as far as i could tell, does nothing, it might just be so the stack is cleared
 - 0x1: CALLVALUE - according to the docs, callvalue takes in some input and pushes it to the stack
 - 0x2: PUSH2 - this pushes 2 bytes to the stack, so now we have `0x1337` or `4919` on the stack and an unknown variable below that
 - 0x5: MUL - this just multiplies the top two values on the stack and pushes the value to the stack
 - 0x6: PUSH6 - now we push 6 bytes onto the stack: `0xfdc29ff358a3` or `279012349008035`
 - 0xd: EQ - This compares the top 2 values on the stack and if they're equal pushes a `1` onto the stack otherwise a `0`
 - 0xe: PUSH1 - now we push a single byte to the stack: `0x12` this represents the address to jump to
 - 0x10: JUMPI - this checks the second value on the stack and if it's `true` or `1`, jumps to the address of the first value on the stack in this case: `0x12` or the `STOP` opcode
 - 0x11: SELFDESTRUCT - this is the opcode we want to avoid according to the description, so we would need to make the `EQ` return true
 - 0x12: STOP - This just signifies the end of the program

so we just analyzed the program line by line, that would be one way to do it, but as the programs get longer it gets much harder to do, so we could instead use a EVM bytecode debugger like [www.evm.codes/playground](https://www.evm.codes/playground?codeType=Mnemonic) 

either way we find that the program multiplies the input with `0x1337` and checks if its equal to `0xfdc29ff358a3` and if it isn't, it self destructs

so to find the answer, we can just divide `0xfdc29ff358a3` by `0x1337` to get `56721355765` or in hex: `0xd34db33f5`

and according to that, we can find the flag: `n00bz{0xd34db33f5}`
