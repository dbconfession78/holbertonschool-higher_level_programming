#!/usr/bin/python3
i = 0
#for i in range(0, 26):#
while i < 26:
    if chr(97+i) != "q" and chr(97+i) != "e":
        print(chr(97+i), end='')
    i = i + 1
