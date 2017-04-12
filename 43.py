"""
Project Euler
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.


author:  Adam Shechter
"""

from itertools import permutations

primes_list = [1, 2, 3, 5, 7, 11, 13, 17]


def main():
    print(sum(sub_string_div()))


def sub_string_div():
    perms_pandigital = ["".join(x) for x in list(permutations('0123456789'))]
    matches = []
    for curr_perm in perms_pandigital:
        print(curr_perm)
        is_divisible = True
        if curr_perm[0:1] == '0':
            continue
        else:
            for i in range(1, 8):
                curr_int = int(curr_perm[i:i+3])
                print(curr_int)
                if curr_int % primes_list[i] != 0:
                    is_divisible = False
                    break
            if is_divisible:
                print("Pandigital Prime Divisible Number: {}".format(curr_perm))
                matches.append(int(curr_perm))
    print("Pandigital Number List:")
    print(matches)
    return matches


if __name__ == '__main__':
    main()
