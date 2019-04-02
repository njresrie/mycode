#!/usr/bin/env python3

my_nums = [-1, "pikachu", 3, "banana", -20, 45, 42, -67]

pos = []
bignum = []
neg = []

for number in my_nums:
    if type(number) is int:
        if number >= 30:
            bignum.append(number)
        elif number >= 0:
            pos.append(number)
        else:
            neg.append(number)
    elif number == "pikachu":
        continue

    else:
        print("{} is not an integer!".format(number))

print("Bignums are: {} ".format(bignum))
print("Positives are: {} ".format(pos))
print("Negatives are: {} ".format(neg))
