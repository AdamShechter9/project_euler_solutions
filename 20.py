"""
Project Euler
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


author:  Adam Shechter
"""

from math import factorial


def main():
    print(factorial_digit_sum(100))


def factorial_digit_sum(n):
    n_fac = factorial(n)
    sum_dig = sum([int(x) for x in str(n_fac)])
    return sum_dig

if __name__ == '__main__':
    main()