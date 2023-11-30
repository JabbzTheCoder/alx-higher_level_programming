#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i) if (ord('z') - i) % 4 < 2 else chr(i - 32)), 
            end="")
