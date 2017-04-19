"""
Project Euler
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be written
as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

author:  Adam Shechter
"""
import math

primes = [2]


def main():
    print(goldbach_conjecture_fail(10000))


def goldbach_conjecture_fail(uplimit):
    failures = []
    for n in range(3, uplimit, 2):
        if is_prime(n):
            print("{} is prime".format(n))
            primes.append(n)
        else:
            # run through primes
            print("{} tested".format(n))
            found_sol = False
            for prime in primes:
                if found_sol:
                    break
                for y in range(1, 100):
                    x = prime + 2 * pow(y, 2)
                    if x == n:
                        print("PASSED {}: {} + 2 * {} ^ 2".format(n, prime, y))
                        found_sol = True
                        break
            if not found_sol:
                print("FOUND ANOMALY")
                failures.append(n)
                # failures.append(n)
    if not failures:
        return False
    else:
        return failures


def is_prime(n):
    # 1 is not a prime
    if n == 1:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    else:
        for i in range(11, math.floor(pow(n, 0.5))+2, 2):
            if n % i == 0:
                return False
    return True


if __name__ == '__main__':
    main()
