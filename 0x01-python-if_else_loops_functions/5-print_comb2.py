#!/usr/bin/python3
for number in range(0, 100, 1):
    if number == 99:
        print("{}".format(number), end="\n")
    else:
        print("{:02}".format(number), end=", ")


