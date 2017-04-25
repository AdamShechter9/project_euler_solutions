"""
Project Euler
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

Solution:
Start with 100 and move up to X upper limit.
Create permutations of every number as a string and test each multiplication.

author:  Adam Shechter
"""
from itertools import permutations


def main():
    permuted_multiples(1000000, 6)


def permuted_multiples(limit2, multiple):
    for n in range(100000, limit2):
        digits_perms = [int("".join(x)) for x in list(permutations(str(n)))]
        # print(n, digits_perms)
        print(n)
        isPass = True
        for i in range(1, multiple+1):
            if not isPass:
                break
            product = i * n
            # print("Test: {}     PRoduct: {}".format(i, product))
            if product not in digits_perms:
                isPass = False
                break
        if isPass:
            print("For {} multiples, Number: {}     keeps same digits".format(multiple, n))
            return n


if __name__ == '__main__':
    main()
