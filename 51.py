"""
Project Euler
Problem 51

By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.



Solution:
We know that the first prime to have the 7 primes property is 5 digits.
So we generate a pool of primes with 5 digits.  (We can create a bigger pool later).

Next, we have a function that takes a number as an input, and runs through combinations of various digit placements,
returning the digit replacement formula with the most primes.



Possible optimizations:
If we're looking for 7 primes property, and are replacing 2 digits,
We can only look for prime numbers that have AT LEAST 2 digits equal or greater to 3 (10-7).
Meaning, if all digits are greater than (10-x) we don't need to test it.



author:  Adam Shechter
"""
import math


def main():
    prime_pool = get_primes(10001, 100000000)
    print(len(prime_pool))
    answers = prime_digit_replacement(prime_pool, 1, 7)
    print(answers)


def prime_digit_replacement(prime_pool, digits, target):
    replace_pool = [x for x in prime_pool if prime_optimization(x, digits, target)]
    # replace_pool = prime_pool
    answers = set()
    for prime in replace_pool:
        len1 = len(str(prime))
        # Single digit replacement
        for i1 in range(len1):
            prime_str = str(prime)
            if int(prime_str[i1:i1+1]) > (10-target):
                continue
            prime_str = prime_str[:i1] + "*" + prime_str[i1+1:]
            result = prime_digit_test(prime_pool, prime_str)
            if result >= 6:
                print("testing: {}      str: {}     result:  {}".format(prime, prime_str, result))
            if result >= target:
                answers.add((prime_str, prime, result))
        # dual digit replacement
        for i1 in range(len1-1):
            prime_str = str(prime)
            if int(prime_str[i1:i1+1]) > (10-target):
                continue
            for i2 in range(i1+1, len1):
                prime_str = str(prime)
                if int(prime_str[i2:i2 + 1]) > (10 - target):
                    continue
                prime_str = prime_str[:i1] + "*" + prime_str[i1+1:]
                prime_str = prime_str[:i2] + "*" + prime_str[i2+1:]
                result = prime_digit_test(prime_pool, prime_str)
                if result >= 6:
                    print("testing: {}      str: {}     result:  {}".format(prime, prime_str, result))
                if result >= target:
                    answers.add((prime_str, prime, result))
        # Triple digit replacement
        for i1 in range(len1-2):
            prime_str = str(prime)
            if int(prime_str[i1:i1+1]) > (10-target):
                continue
            for i2 in range(i1+1, len1-1):
                prime_str = str(prime)
                if int(prime_str[i2:i2 + 1]) > (10 - target):
                    continue
                for i3 in range(i2+1, len1):
                    prime_str = str(prime)
                    if int(prime_str[i3:i3 + 1]) > (10 - target):
                        continue
                    prime_str = prime_str[:i1] + "*" + prime_str[i1+1:]
                    prime_str = prime_str[:i2] + "*" + prime_str[i2+1:]
                    prime_str = prime_str[:i3] + "*" + prime_str[i3+1:]
                    result = prime_digit_test(prime_pool, prime_str)
                    if result >= 6:
                        print("testing: {}      str: {}     result:  {}".format(prime, prime_str, result))
                    if result >= target:
                        answers.add((prime_str, prime, result))
    return answers


def prime_digit_test(prime_pool, prime_str):
    counts = 0
    for n in range(10):
        test1 = prime_str.replace("*", str(n))
        if int(test1) in prime_pool:
            counts += 1
    return counts


def prime_optimization(x, digits, target):
    counter = 0
    for chr1 in str(x):
        if int(chr1) <= (10 - target):
            counter += 1
        if counter >= digits:
            return True
    return False


def get_primes(lim1, lim2):
    primes = []
    for n in range(lim1, lim2+1, 2):
        if is_prime(n):
            primes.append(n)
    return primes


def is_prime(n):
    # 1 is not a prime
    if n == 1:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    else:
        for i in range(11, int(math.floor(pow(n, 0.5)) + 2), 2):
            if n % i == 0:
                return False
    return True

if __name__ == '__main__':
    main()
