"""
Project Euler
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?

Solution
start with 3 (2nd prime) and move up the odd numbers checking for primes using our exising prime list,
and add to list when you find a new one until you reach the series.

author:  Adam Shechter
"""


def main():
    print(find_primes(10001))


def find_primes(index):
    primes = [2, 3]
    x = 3
    while len(primes) < index:
        x += 2
        for p in primes:
            if x % p == 0:
                break
        else:
            primes.append(x)
    print(primes)
    return primes[index-1]


if __name__ == '__main__':
    main()