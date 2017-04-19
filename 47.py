"""
Project Euler
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?



author:  Adam Shechter
"""
import math


def main():
    print(consecutive_distinct_primes(4, 500000))


def consecutive_distinct_primes(size, uprange):
    prev_distinct_primes = 0
    consecutive = 0
    for i in range(14, uprange):
        distinct_primes = get_primes(i)
        print(i, distinct_primes)
        if prev_distinct_primes != len(distinct_primes):
            prev_distinct_primes = len(distinct_primes)
            consecutive = 0
        else:
            if prev_distinct_primes == size:
                consecutive += 1
        if consecutive + 1 == size:
            return i - consecutive, i


def get_primes(original_x):
    PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

    # print("Number: {}".format(original_x))
    primes_x = []
    x = original_x
    while True:
        found_p = False
        for n_prime in PRIMES:
            if x % n_prime == 0:
                if x / n_prime != 1:
                    x /= n_prime
                    # print("prime {}     remainder {}".format(n_prime, x))
                    primes_x.append(n_prime)
                    found_p = True
                    break
                else:
                    # print("prime {}     remainder {}".format(n_prime, x))
                    primes_x.append(n_prime)
                    return set(primes_x)
        if not found_p:
            # print("searching for primes greater than 100")
            for n in range(101, int(x)+1, 2):
                if x % n == 0:
                    if x / n != 1:
                        x /= n
                        # print("prime {}     remainder {}".format(n, x))
                        primes_x.append(n)
                        break
                    else:
                        # print("prime {}     remainder {}".format(n, x))
                        primes_x.append(n)
                        return set(primes_x)

if __name__ == '__main__':
    main()
