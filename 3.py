"""
Project Euler
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Solution
Check for prime numbers by dividing number with primes [2,3,5,7,11,13,17,19,23,29,...] until we reach a number
indivisible except by itself and 1.




author:  Adam Shechter
"""


def main():
    print(get_primes(13195))
    print(get_primes(11254653))
    print(get_primes(5464574386))
    print(get_primes(600851475143))


def get_primes(original_x):
    PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

    print("Puzzle Number: {}".format(original_x))
    primes_x = []
    x = original_x
    while True:
        found_p = False
        for n_prime in PRIMES:
            if x % n_prime == 0:
                if x / n_prime != 1:
                    x /= n_prime
                    print("prime {}     remainder {}".format(n_prime, x))
                    primes_x.append(n_prime)
                    found_p = True
                    break
                else:
                    print("prime {}     remainder {}".format(n_prime, x))
                    primes_x.append(n_prime)
                    return primes_x
        if not found_p:
            print("searching for primes greater than 100")
            for n in range(101, int(x)+1, 2):
                if x % n == 0:
                    if x / n != 1:
                        x /= n
                        print("prime {}     remainder {}".format(n, x))
                        primes_x.append(n)
                        break
                    else:
                        print("prime {}     remainder {}".format(n, x))
                        primes_x.append(n)
                        print("done.")
                        return primes_x


if __name__ == '__main__':
    main()