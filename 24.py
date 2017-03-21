"""
Project Euler
Problem 24

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

author:  Adam Shechter
"""

from itertools import permutations

def main():
    perms = calc_perms("0123456789")
    # print(perms)
    print(perms[999999])

def calc_perms(a):
    perms = []
    perm_iter = permutations(a)
    while True:
        try:
            curr_perm = next(perm_iter)
            perms.append(curr_perm)
            # print(curr_perm)
        except StopIteration:
            break
    return perms



if __name__ == '__main__':
    main()