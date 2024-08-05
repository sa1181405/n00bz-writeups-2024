# Vinegar 2
Writeup author: taodragon_

Point count: 135pts

Provided files:
- chall.py
- enc.txt

Description:
>Never limit yourself to only alphabets! Author: NoobMaster

# 

The code looks complicated, but it actually does something simple.
It starts with this code segment:
```
alphanumerical = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(){}_?'
matrix = []
for i in alphanumerical:
	matrix.append([i])

idx=0
for i in alphanumerical:
	matrix[idx][0] = (alphanumerical[idx:len(alphanumerical)]+alphanumerical[0:idx])
	idx += 1
```
This code creates an array of arrays of strings such that `matrix[x][0][y]` is the same as `alphanumerical[x+y]`.
Then we get this code:
```
flag_arr = []
key_arr = []
enc_arr=[]
for y in flag:
	for i in range(len(alphanumerical)):
		if matrix[i][0][0]==y:
			flag_arr.append(i)

for y in key:
	for i in range(len(alphanumerical)):
		if matrix[i][0][0]==y:
			key_arr.append(i)
```
We know that `matrix[i][0][0]` is the same as `alphanumerical[i]`, so this is just converting the flag and key to an array of indexes of each letter in `alphanumerical`.
Then this code segment:
```
for i in range(len(flag)):
	enc_arr.append(matrix[flag_arr[i]][0][key_arr[i]])
encrypted=''.join(enc_arr)
```
Because `matrix[x][0][y]` is the same as `matrix[x+y]`, we see that this is just adding each int in `flag_arr` and `key_arr` and adding the character at that value in `alphanumerical` to encrypted, which is written to enc.txt

Therefore, we need to convert each character in encrypted and the key to an int by getting the index of each character in `alphanumerical`. Then we subtract each key index from the corresponding ciphertext index. Then we convert it back to a string to get the flag.

Script: `sol.py`
Flag: `n00bz{4lph4num3r1c4l_1s_n0t_4_pr0bl3m}`
