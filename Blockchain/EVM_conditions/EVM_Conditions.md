# EVM: Conditions
Point count: 4__

Provided files: `evm.txt`

**Description:** So much maths... You need to find the value, in hex, that you need to send to make the contract STOP and not self destruct. Wrap the hex in `n00bz{}`. If the correct answer is 9999, the flag is `n00bz{0x270f}`. Author: NoobMaster

Using a decompiler like [this one](https://ethervm.io/decompile), decompile from Solidity to bytecode.
```
[0] PUSH0 0x
[1] PUSH1 0x0f
[2] PUSH1 0x70
[3] MUL
[4] PUSH2 0x0258
[5] MSTORE
[6] PUSH0 0x
[7] PUSH1 0x05
[8] PUSH1 0x96
[9] DIV
[10] PUSH1 0x90
[11] MSTORE
[12] PUSH0 0x
[13] PUSH1 0x07
[14] PUSH1 0x09
[15] EXP
[16] PUSH2 0xFFFA
[17] MSTORE
[18] PUSH2 0x0539
[19] PUSH2 0x26aa
[20] XOR
[21] PUSH3 0x0bfabf
[22] MSTORE
[23] PUSH1 0x03
[24] PUSH2 0xfffa
[25] MLOAD
[26] MUL
[27] PUSH3 0x0bfabf
[28] MLOAD
[29] ADD
[30] CALLVALUE
[31] PUSH2 0x0258
[32] MLOAD
[33] PUSH1 0x04
[34] MUL
[35] ADD
[36] PUSH1 0x90
[37] MLOAD
[38] ADD
[39] EQ
[40] PUSH1 0x48
[41] JUMPI
[42] SELFDESTRUCT
[43] STOP 
```
Now, it's just a matter of simulating the actions on the stack. The meanings of each opcode can be found [here](https://ethereum.org/en/developers/docs/evm/opcodes/) or [here](https://ethervm.io/#opcodes).


First, 0x0f and 0x70 are pushed, then multiplied, resulting in 0x0690.

0x0258 is pushed and 0x0690 is stored at that memory address.

(MSTORE stores the second value at the memory address given by the top value.)
0x05 and 0x96 are pushed, then divided, resulting in 0x1e.

0x90 is pushed and 0x1e is stored at that memory address.

0x07 and 0x09 are pushed, and exponentiated (top number is base, so 9^7), resulting in 0x48fb79.

0xfffa is pushed and 0x48fb79 is stored at that memory address.

0x0539 and 0x26aa are pushed, then XOR'd, resulting in 0x2393.

0x0bfabf is pushed, and 0x2393 is stored at that memory address.

We have just completed [22] and have the following in memory:


0x0690 at 0x0258

0x1e at 0x90

0x48fb79 at 0xfffa

0x2393 at 0x0bfabf


Continuing, 0x03 and 0xfffa are pushed, then MLOAD is used to replace the top value of the stack with what is stored at the corresponding memory address.

The top of the stack is [0xfffa, 0x03] and becomes [0x48fb79, 0x03] since 0x48fb79 was stored at 0xfffa in memory.

The top two values are multiplied to obtain 0xdaf26b.

Then, 0x0bfabf is pushed and loaded, become 0x2393, and added to 0xdaf26b, resulting in 0xdb15fe.

Next, CALLVALUE takes an input. The objective is to find what input will prevent self-destruction.

For now, let this input be N. The top of the stack is [N, 0xdb15fe].

0x0258 is pushed and loaded, becoming 0x0690.

0x04 is pushed and multiplied with this, resulting in 0x1a40.

The top of the stack is now [0x1a40, N, 0xdb15fe].

The top two are added, resulting in a stack of [0x1a40 + N, 0xdb15fe], then 0x90 is pushed and loaded, becoming 0x1e.

The top two are added again, resulting in [0x1a5e + N, 0xdb15fe].

Using EQ transforms the top two into either 0 or 1 depending on if they are equal.

Let this boolean value be M. 0x48 is pushed, so the top of the stack is [0x48, M].

Finally, we arrive at the last few lines.
JUMPI will jump to the line with number given by the top of the stack, or 0x48 = 72, if the condition given by the second value, M, is met. If M is 0, we will proceed to [42] SELFDESTRUCT which is not what we want. So, we must have 0x1a5e + N = 0xdb15fe, or N = 0xdafba0.

Final flag: `n00bz{0xdafba0}`
