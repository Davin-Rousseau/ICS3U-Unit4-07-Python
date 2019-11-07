#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on November 2019
# This program uses nested loops
# To print out all possible RGB combinations


def main():
    # This function Calculates all RGB combinations
    loop_counter = 1

    # process and output
    for numbers in range(1000, 2001):
        loop_counter += 1
        if loop_counter % 5 == 1:
            print("{} ".format(numbers))
        else:
            print("{} ".format(numbers), end="")


if __name__ == "__main__":
    main()
