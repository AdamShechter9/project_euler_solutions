"""
Project Euler
Problem 53

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

author:  Adam Shechter
"""
import math

def main():
    ans1 = combinatorics(5, 3)
    ans2 = combinatorics(23, 10)
    print(ans1)
    print(ans2)
    ans3 = combinatorics_selections(1000000)
    print(ans3)


def combinatorics_selections(limit1):
    count = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            result = combinatorics(n, r)
            if result > limit1:
                count += 1
                print("n: {}    r: {}   result: {}      ****************".format(n,r, result))
            else:
                print("n: {}    r: {}   result: {}".format(n,r,result))
    return count


def combinatorics(n, r):
    result = math.factorial(n) / (math.factorial(r) * math.factorial(n-r))
    return int(result)

if __name__ == '__main__':
    main()