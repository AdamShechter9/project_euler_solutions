"""
Project Euler
Problem 26
Reciprocal cycles

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains
the longest recurring cycle in its decimal fraction part.


author:  Adam Shechter
"""

from decimal import *
MAX_CHARS = 1000000
getcontext().prec = MAX_CHARS


def main():
    print(find_longest_cycle(1000))


def find_longest_cycle(range_limit):
    max_len = 0
    max_str = ""
    max_n = -1
    for i in range(2, range_limit):
        print(i, end=" ")
        result = decimal_division(i)
        if len(str(result)) >= MAX_CHARS+2:
            cycle_len, cycle_str = find_recurring_cycle(result)
            print("cycle length {}".format(cycle_len))
            if cycle_len > max_len:
                max_len = cycle_len
                max_str = cycle_str
                max_n = i
        else:
            print("Not infinite fraction.")
        print("*" * 25)
    return max_n, max_len, max_str


def find_recurring_cycle(n):
    dec_str = str(n)
    dec_str = dec_str[2:]
    found_cycle = False
    index = 0
    while not found_cycle:
        cycle_str = ""
        for c in dec_str[index:]:
            cycle_str += c
            chr_count = dec_str.count(cycle_str)
            # print("string: {}       chr: {}      count: {}      index: {}".format(cycle_str, c, chr_count, index))
            if chr_count >= ((MAX_CHARS - index - 1) // len(cycle_str)) or chr_count >= ((MAX_CHARS - index) // len(cycle_str)):
                found_cycle = True
                break
            elif chr_count == 1:
                print(" | ")
                index += 1
                break
            else:
                pass
    print("cycle: {}".format(cycle_str))
    cycle_len = len(cycle_str)
    return cycle_len, cycle_str


def decimal_division(n):
    numerator = Decimal(1)
    denominator = Decimal(n)
    result = numerator / denominator
    return result


if __name__ == '__main__':
    main()