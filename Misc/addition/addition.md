# Addition
Writeup author: **wjat**
Point count: 100

Provided files: [server.py](https://static.n00bzunit3d.xyz/Misc/Addition/server.py)

Description: My little brother is learning math, can you show him how to do some addition problems? Author: Connor Chang

# Solution
At the beginning, the user inputs a number of questions, stored in the variable `questions`. Then, there is a loop using `for i in range(questions):`. At the end, the flag is partially printed: `print(flag[:questions])`. There is no check on questions, so putting in -1 bypasses the loop and the full flag prints without any addition questions answered.

Final flag: `n00bz{m4th_15nt_4ll_4b0ut_3qu4t10n5}`