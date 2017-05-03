#!/usr/bin/python3
for i in range(0, 26):
    if i % 2 == 0:
        print(chr(122-i))
    else:
        print(chr(122-i-32))
