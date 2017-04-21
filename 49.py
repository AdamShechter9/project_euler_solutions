"""
Project Euler
Problem 49
Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

author:  Adam Shechter
"""

from itertools import permutations
import math


def main():
    print(prime_permutations(4))


def prime_permutations(dig_len):
    four_digit_primes = []
    answers = []
    for n in range(1000, 10000):
        if is_prime(n):
            four_digit_primes.append(n)
    for prime in four_digit_primes:
        prime_perms = set()
        all_prime_perms = [int("".join(x)) for x in list(permutations(str(prime)))]
        # print(all_prime_perms)
        for prime2 in all_prime_perms:
            if prime2 in four_digit_primes:
                prime_perms.add(prime2)
            prime_perms2 = sorted(prime_perms)
            for i1 in range(len(prime_perms2)-1):
                for i2 in range(i1+1, len(prime_perms2)-1):
                    prime_diff = abs(prime_perms2[i1] - prime_perms2[i2])
                    if (prime_perms2[i2] + prime_diff) in prime_perms2:
                        answer_tuple = (prime_perms2[i1], prime_perms2[i2], prime_perms2[i2] + prime_diff)
                        if answer_tuple not in answers:
                            answers.append(answer_tuple)
    return answers


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
