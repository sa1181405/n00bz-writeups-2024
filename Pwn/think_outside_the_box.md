# Addition
Writeup author: **wjat**
Point count: 464

Provided files: [thinkoutsidethebox.zip](https://static.n00bzunit3d.xyz/Pwn/Think-outside-the-Box/thinkoutsidethebox.zip)

Description: You cannot beat my Tic-Tac-Toe bot! If you do, you get a flag! Author: NoobMaster

# Solution
Using IDA to check the source code, we find that move input is taken in the form x,y where x and y are integers and 1,1 is the center of the board. However, x and y are never checked, so the bot can easily be confused by playing, literally, "outside the box." One such winning sequence is "0,-1", "0,0", "0,1", "0,2".

Final flag: `n00bz{l173r4lly_0u7s1d3_7h3_b0x_L0L_5807310a178d}`