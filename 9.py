"""
Project Euler
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Solution:
Brute force:
Knowing the sum is 1000, we can start checking for the solution by 1^2 + 2^2 = (1000-1-2)^2
and incrementing b while decrementing c.  When b is equal to c, we increment a 1, and repeat
until we find solution.

author:  Adam Shechter
"""

from functools import reduce


def main():
    triplet = find_pyth_triplet(1000)
    print(reduce(lambda x, y: x*y, triplet))


def find_pyth_triplet(sum1):
    for a in range(1, sum1):
        a2 = pow(a, 2)
        for b in range(a+1, sum1):
            b2 = pow(b, 2)
            c = sum1-a-b
            c2 = pow(c, 2)
            if (a2 + b2) == c2:
                print("******************* FOUND **********************")
                return [a, b, c]
    return [0]

if __name__ == '__main__':
    main()