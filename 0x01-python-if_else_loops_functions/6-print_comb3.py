#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1+i, 10):
            print(i, end='')
            if i != 8:
                print(j, end=', ')
            else:
                print(j)
