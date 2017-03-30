"""
Project Euler
Problem 35

Circular primes

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?


Solution:
test all permutations of number 'n' for primeness.
Optimization: You can add future permutations to the list and skip. for example, 113 returns true,
so add 131 and 311 to list.

author:  Adam Shechter
"""


def main():
    circ_primes = circular_primes(1000000)
    print("list: {} \ncount: {}     sum: {}".format(circ_primes, len(circ_primes), sum(circ_primes)))


def circular_primes(range2):
    circ_primes = [2]
    reject_nums = []
    current_dig = 1
    for n in range(2, range2):
        if n % 2 == 0:
            continue
        if n in circ_primes or n in reject_nums:
            continue
        if len(str(n)) > current_dig:
            print("New Digits: {}".format(n))
            current_dig += 1
        if len(str(n)) < 2:
            if is_prime(n):
                circ_primes.append(n)
        else:
            n_rotation = rotations(str(n))
            # print(n_rotation)
            for n_perm in n_rotation:
                if not is_prime(n_perm):
                    reject_nums += n_rotation
                    break
            else:
                circ_primes += n_rotation
                print("FOUND******* {}".format(n))

    return set(circ_primes)


def rotations(str_x):
    output = []
    for i in range(len(str_x)):
        output.append(int(str_x[i:] + str_x[:i]))
    return output


def is_prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0:
        return False
    else:
        for i in range(13, n, 2):
            if n % i == 0:
                return False
    return True

if __name__ == '__main__':
    main()
