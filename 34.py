"""
Project Euler
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

author:  Adam Shechter
"""

from math import factorial


def main():
    dig_facts = digit_factorials()
    print(dig_facts)
    print(sum(dig_facts))


def digit_factorials():
    digit_facts = []
    for i in range(10, 100000):
        i_str = str(i)
        dig_fact_sum = sum([factorial(int(x)) for x in i_str])
        if i == dig_fact_sum:
            digit_facts.append(i)
            print(i, dig_fact_sum)
    return digit_facts

if __name__ == '__main__':
    main()