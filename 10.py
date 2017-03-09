"""
Project Euler
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.


Solution:
Brute Force = Use previous solution to compile a list of all primes under 2,000,000.
Print Sum of prime list.

author:  Adam Shechter
"""


def main():
    # print(find_primes(10))
    print(find_primes(2000000))


def find_primes(limit):
    primes = [2, 3]
    x = 3
    while x < (limit-1):
        x += 2
        for p in primes:
            if x % p == 0:
                break
        else:
            print(x, end=" ")
            primes.append(x)
    print(primes)
    return sum(primes)


if __name__ == '__main__':
    main()