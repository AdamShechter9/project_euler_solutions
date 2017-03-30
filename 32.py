"""
Project Euler
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


Solution
--------
One way would be to multiply x * xxx = xxxxx from 1 * 234 = 56789 to 9 * 876 = 54321
and increase digits to 12 * 345 = 6789 and 98 * 765 = 4321
By generating permutations of string '123456789' we can minimize operations to smallest number.


author:  Adam Shechter
"""

from itertools import permutations


def main():
    pandigital_products1 = pandigital_products('123456789')
    print(sum(pandigital_products1))


def pandigital_products(sequence):
    seq_perms = permutations(sequence)
    win_seqs = []
    while 1:
        try:
            test_perm = next(seq_perms)
            # print(test_perm)
            # 1 digit * 4 digit = 4 digit
            # 2 digit * 3 digit = 4 digit
            # 3 digit * 2 digit = 4 digit
            # 4 digit * 1 digit = 4 digit
            product3 = int("".join(test_perm[-4:]))
            mults = test_perm[:-4]
            for i in range(1, 5):
                mult1 = int("".join(mults[:i]))
                mult2 = int("".join(mults[i:]))
                # print("testing: {} * {} = {}".format(mult1, mult2, product3))
                if mult1 * mult2 == product3:
                    print("*********************** FOUND **************", product3)
                    if product3 not in win_seqs:
                        win_seqs.append(product3)
        except StopIteration:
            break
    return win_seqs



if __name__ == '__main__':
    main()