#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i < j:
            print("{:02d}{:02d}".format(i, j), end=", " if j < 9 or i < 8 else "\n")
