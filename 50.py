"""
Project Euler
Problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

author:  Adam Shechter
"""
import math

def main():
    print(consecutive_prime_sum(1000))
    print(consecutive_prime_sum(10000))
    print(consecutive_prime_sum(100000))
    print(consecutive_prime_sum(1000000))


def consecutive_prime_sum(limit):
    prime_pool = []
    for n in range(2, limit):
        if is_prime(n):
            prime_pool.append(n)
    max_sum = 0
    max_seq = []
    for i1 in range(len(prime_pool)-1):
        for i2 in range(len(prime_pool)):
            curr_slice = prime_pool[i1:i2]
            curr_sum = sum(curr_slice)
            if curr_sum > limit:
                break
            if curr_sum < limit and len(max_seq) < len(curr_slice):
                if curr_sum in prime_pool:
                    max_sum = curr_sum
                    max_seq = prime_pool[i1:i2]
                    print("MAX SUM {}   MAX LEN {}\nMAX SEQ {}".format(max_sum, len(max_seq), max_seq))
        if prime_pool[i1] > limit:
            break
    return max_sum, max_seq


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
