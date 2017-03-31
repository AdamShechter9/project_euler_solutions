"""
Project Euler
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

author:  Adam Shechter
"""
from itertools import permutations


def main():
    pandigitals = pandigital_multiples('123456789')
    print(pandigitals)


def pandigital_multiples(digits1):
    digits_perms = ["".join(x) for x in list(permutations(digits1))]
    products_list = []
    for i in range(1, 10000):
        product = ""
        j = 1
        while len(product) < 9:
            prod = i * j
            product += str(prod)
            j += 1
        if len(product) == 9:
            # print(product)
            if product in digits_perms:
                print("number: {}       product: {}".format(i, product))
                products_list.append(product)
    return sorted(products_list)

if __name__ == '__main__':
    main()