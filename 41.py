"""
Project Euler
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

author:  Adam Shechter
"""
from itertools import permutations
import math


def main():
    print(greatest_pandigital_prime_lexigraphic('1234567890'))


def greatest_pandigital_prime_lexigraphic(digits1):
    while len(digits1) > 1:
        digits_perms = sorted([int("".join(x)) for x in list(permutations(digits1))], reverse=True)
        answer_list = []
        for n in digits_perms:
            print(n)
            if is_prime(n):
                answer_list.append(n)
                print("******* FOUND PRIME ********   {}".format(n))
        if not answer_list:
            digits1 = digits1[:-1]
        else:
            break
    return sorted(answer_list, lambda x: int(x))


def is_prime(n):
    # 1 is not a prime
    if n == 1:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    else:
        for i in range(11, math.floor(pow(n, 0.5))+1, 2):
            if n % i == 0:
                return False
    return True

if __name__ == '__main__':
    main()