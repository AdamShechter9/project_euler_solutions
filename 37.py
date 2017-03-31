"""
Project Euler
Problem 37

The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


author:  Adam Shechter
"""


def main():
    trunc_primes = truncate_primes(1000000)
    print(trunc_primes)
    print(len(trunc_primes))
    print(sum(trunc_primes))


def truncate_primes(range1):
    answers = []
    digit = 2
    for i in range(11, range1, 2):
        if len(str(i)) > digit:
            digit += 1
            print(i)
        i_str = str(i)
        if i_str[:1] == '1' or i_str[-1:] == '1':
            continue
        if is_prime(i):
            trunc_left = False
            trunc_right = False
            iStr = str(i)
            while len(iStr) > 1:
                iStr = iStr[1:]
                if not is_prime(int(iStr)):
                    break
            else:
                # print("Trunc Left: {}".format(i))
                trunc_left = True
            iStr = str(i)
            while len(iStr) > 1:
                iStr = iStr[:-1]
                if not is_prime(int(iStr)):
                    break
            else:
                # print("Trunc Right: {}".format(i))
                trunc_right = True
            if trunc_left and trunc_right:
                print("FOUND****** {}".format(i))
                answers.append(i)
        else:
            continue
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
        for i in range(11, n, 2):
            if n % i == 0:
                return False
    return True

if __name__ == '__main__':
    main()
