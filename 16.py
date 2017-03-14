"""
Project Euler
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?\

author:  Adam Shechter
"""


def main():
    print(power_digit_sum(1000))


def power_digit_sum(expo):
    return sum([int(x) for x in str(pow(2, expo))])

if __name__ == '__main__':
    main()
