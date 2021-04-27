#!/usr/bin/python3

alpha = []

for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        alpha.append(chr(i))
    else:
        alpha.append(chr(i - 32))
for i in range(len(alpha)):
    print("{}".format(alpha[i]), end="")
