"""
Project Euler
Problem 40


An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

author:  Adam Shechter
"""


def main():
    c_const = champernowne_constant()
    print(champernowne_constant_product(c_const, 7))


def champernowne_constant_product(c_const, exp):
    multiplier = 0
    product = 1
    while multiplier < exp:
        char1 = c_const[pow(10, multiplier) - 1]
        product *= int(char1)
        multiplier += 1
    return product


def champernowne_constant():
    const_str = ""
    for i in range(1, 1000001):
        const_str += str(i)
    return const_str


if __name__ == '__main__':
    main()
