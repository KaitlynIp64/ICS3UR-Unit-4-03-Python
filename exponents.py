#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program calculates the exponent of an integer

import random


def main():
    # this is an exponents calculator
    loop_counter = 0
    answer = 1

    # input
    str_integer = input("Enter a positive integer: ")

    # process
    try:
        int_integer = int(str_integer)
        if int_integer < 0:
            print("This is not a positive number.")
        for loop_counter in range(int_integer + 1):
            answer = loop_counter * loop_counter
            print("{0}² = ".format(loop_counter) + "{0}.".format(answer))
    except ValueError:
        print("That is not a valid input.")
    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
