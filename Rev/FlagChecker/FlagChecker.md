# FlagChecker
**Writeup Author:** wjat
**Original Solver:** wjat
**Point Value:** 431

**Provided Files:**
[FlagChecker.xlsm](https://static.n00bzunit3d.xyz/Rev/FlagChecker/FlagChecker.xlsm)

**Description:**
Why did the macros hide its knowledge? Because it didn't want anyone to "excel"! Note: `char_21` is the SAME as `char_22` Note 2: The correct flag has ALL LOWERCASE, NUMBERS, `n00bz{}` AND UNDERSCORES (There's two underscores in the entire flag) Author: NoobMaster

# Solution
The file is a `.xlsm` file, meaning it has a macro or macros. Source code for the macro (VBScript):
```vbs
Sub FlagChecker()

    Dim chars(1 To 24) As String
    guess = InputBox("Enter the flag:")
    If Len(guess) <> 24 Then
        MsgBox "Nope"
    End If
    char_1 = Mid(guess, 1, 1)
    char_2 = Mid(guess, 2, 1)
    char_3 = Mid(guess, 3, 1)
    char_4 = Mid(guess, 4, 1)
    char_5 = Mid(guess, 5, 1)
    char_6 = Mid(guess, 6, 1)
    char_7 = Mid(guess, 7, 1)
    char_8 = Mid(guess, 8, 1)
    char_9 = Mid(guess, 9, 1)
    char_10 = Mid(guess, 10, 1)
    char_11 = Mid(guess, 11, 1)
    char_12 = Mid(guess, 12, 1)
    char_13 = Mid(guess, 13, 1)
    char_14 = Mid(guess, 14, 1)
    char_15 = Mid(guess, 15, 1)
    char_16 = Mid(guess, 16, 1)
    char_17 = Mid(guess, 17, 1)
    char_18 = Mid(guess, 18, 1)
    char_19 = Mid(guess, 19, 1)
    char_20 = Mid(guess, 20, 1)
    char_21 = Mid(guess, 21, 1)
    char_22 = Mid(guess, 22, 1)
    char_23 = Mid(guess, 23, 1)
    char_24 = Mid(guess, 24, 1)
    If (Asc(char_1) Xor Asc(char_8)) = 22 Then
        If (Asc(char_10) + Asc(char_24)) = 176 Then
            If (Asc(char_9) - Asc(char_22)) = -9 Then
                If (Asc(char_22) Xor Asc(char_6)) = 23 Then
                    If ((Asc(char_12) / 5) ^ (Asc(char_3) / 12)) = 130321 Then
                        If (char_22 = char_11) Then
                            If (Asc(char_15) * Asc(char_8)) = 14040 Then
                                If (Asc(char_12) Xor (Asc(char_17) - 5)) = 5 Then
                                    If (Asc(char_18) = Asc(char_23)) Then
                                        If (Asc(char_13) Xor Asc(char_14) Xor Asc(char_2)) = 121 Then
                                            If (Asc(char_14) Xor Asc(char_24)) = 77 Then
                                                If 1365 = (Asc(char_22) Xor 1337) Then
                                                    If (Asc(char_10) = Asc(char_7)) Then
                                                        If (Asc(char_23) + Asc(char_8)) = 235 Then
                                                            If Asc(char_16) = (Asc(char_17) + 19) Then
                                                                If (Asc(char_19)) = 107 Then
                                                                    If (Asc(char_20) + 501) = (Asc(char_1) * 5) Then
                                                                        If (Asc(char_21) = Asc(char_22)) Then
                                                                            MsgBox "you got the flag!"
                                                                        End If
                                                                    End If
                                                                End If
                                                            End If
                                                        End If
                                                    End If
                                                End If
                                            End If
                                        End If
                                    End If
                                End If
                            End If
                        End If
                    End If
                End If
            End If
        End If
    End If
End Sub
```
We obtain the following conditions:
```
A | Asc(char_1) Xor Asc(char_8) = 22
B | Asc(char_10) + Asc(char_24) = 176
C | Asc(char_9) - Asc(char_22) = -9
D | Asc(char_22) Xor Asc(char_6) = 23
E | (Asc(char_12) / 5) ^ (Asc(char_3) / 12) = 130321
F | char_22 = char_11
G | Asc(char_15) * Asc(char_8) = 14040
H | Asc(char_12) Xor (Asc(char_17) - 5) = 5
I | Asc(char_18) = Asc(char_23)
J | Asc(char_13) Xor Asc(char_14) Xor Asc(char_2) = 121
K | Asc(char_14) Xor Asc(char_24) = 77
L | 1365 = Asc(char_22) Xor 1337
M | Asc(char_10) = Asc(char_7)
N | Asc(char_23) + Asc(char_8) = 235
O | Asc(char_16) = Asc(char_17) + 19
P | Asc(char_19) = 107
Q | Asc(char_20) + 501 = (Asc(char_1) * 5)
R | Asc(char_21) = Asc(char_22)
```
We can deduce the value of each character as such:
```
char_1-6 and char_24: flag format
char_24 --> char_10 --> char_7: B, M
char_1 --> char_8: A
char_22 --> char_9: L, C 
char_24 --> char_10: B
char_22 --> char_11: L, F
char_3 --> char_12: E
char_24 --> char_14 --> char_13: K, J
char_24 --> char_14: K
char_1 --> char_8 --> char_15: A, G
char_3 --> char_12 --> char_17 --> char_16: E, H, O
char_3 --> char_12 --> char_17: E, H
char_1 --> char_8 --> char_23 --> char_18: A, N, I 
char_19: P
char_1 --> char_20: Q
char_22 --> char_21: L, R
char_22: L
char_1 --> char_8 --> char_23: A, N
```

Final flag:
`n00bz{3xc3l_y0ur_sk1lls}`