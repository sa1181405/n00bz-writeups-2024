# Random
Writeup author: **wjat**
Point count: 451

Provided files: [server.cpp](https://static.n00bzunit3d.xyz/Crypto/Random/server.cpp)

Description: I hid my password behind an impressive sorting machine. The machine is very luck based, or is it?!?!?!? Author: Connor Chang

# Solution
The source code uses `random_shuffle()`, which shuffles the same way each time the program is run. For example, the first shuffle of `0123456789` is always `4378052169`, and the way the shuffling works is also retained each time the program is run. So, when shuffling a string of length 10, the 0th character will always become the 4th. The method `` returns true only if one if the 69 shuffles produces a string in lexigraphical order.
```cpp
bool good = true;
for (int i = 0; i < n - 1; i++)
    good &= s[i] <= s[i + 1];

if (good)
    return true;
```
This is needed to print the flag.
```cpp
if (amazingcustomsortingalgorithm(s)) {
    ifstream fin("flag.txt");
    string flag;
    fin >> flag;
    cout << flag << endl;
}
```
We also need our input string to be at least 10 characters long and have no repeating characters.
```cpp
for (char c : s) {
    if (counts[c]) {
        cout << "no repeating letters allowed passed this machine" << endl;
        return 1;
    }
    counts[c]++;
}
```
```cpp
if (s.size() < 10) {
    cout << "this machine will only process worthy strings" << endl;
    return 1;
}
```
From here, it's pretty simple to construct a string that will shuffle into order right away. Since `0123456789` becomes `4378052169`, we replace `4` with `A`, `3` with `B`, and so on. The pre-shuffle string after this replacement is `EHGBAFICDJ`. Putting this in yields the flag.

Final flag: `n00bz{5up3r_dup3r_ultr4_54f3_p455w0rd_fe55a38e0f4e}`