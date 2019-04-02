#!/usr/bin/env python3

my_nums = [-1, 3, "banana", -20, 45, 42, -67]

pos = []

neg = []

for number in my_nums:
    if type(number) is int:
        if number >= 0:
            pos.append(number)
        else:
            neg.append(number)
    else:
        print("{} is not an integer!".format(number))

print("Positives are: {} ".format(pos))
print("Negatives are: {} ".format(neg))
