#!/usr/bin/python3
for i in range(0, 26):
    print("{:s}".format(chr(122-i) if i % 2 == 0
                        else chr(122-i-32)), end='')
