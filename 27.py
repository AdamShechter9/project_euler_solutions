"""
Project Euler
Problem 27

Euler discovered the remarkable quadratic formula:

n2+n+41n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤390≤n≤39.
However, when n=40,402+40+41=40(40+1)+41 is divisible by 41,
and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered,
which produces 80 primes for the consecutive values 0 ≤ n ≤ 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces
the maximum number of primes for consecutive values of n, starting with n=0.


author:  Adam Shechter
"""


def main():
    print(quadratic_primes(1000))


def quadratic_primes(limit_range):
    max_primes = 0
    max_coef = {"a": None, "b": None}
    print("Formula: n^2 + an + b")
    for a in range(-limit_range+1, limit_range):
        for b in range(-limit_range-1, limit_range+1):
            n = 0
            num_primes = 0
            while 1:
                result = pow(n, 2) + a*n + b
                if result < 0:
                    break
                if not is_prime(result):
                    break
                else:
                    # print("n: {}    Result: {}   ".format(n, result))
                    num_primes += 1
                    n += 1

            if num_primes > max_primes:
                max_primes = num_primes
                max_coef['a'] = a
                max_coef['b'] = b
                print("a: {}    b: {}       primes: {}".format(a, b, num_primes))
            if num_primes:
                pass
    return max_primes, max_coef


def is_prime(n):
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0:
        return False
    else:
        for i in range(13, n, 2):
            if n % i == 0:
                return False
    return True

if __name__ == '__main__':
    main()
