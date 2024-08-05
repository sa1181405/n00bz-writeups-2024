an = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(){}_?'
key = '5up3r_s3cr3t_k3y_f0r_1337h4x0rs_r1gh7?'
enc = '*fa4Q(}$ryHGswGPYhOC{C{1)&_vOpHpc2r0({'
for i in range(len(enc)):
    print(an[(an.index(enc[i]) - an.index(key[i])) % len(an)], end='')
