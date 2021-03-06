"""
Project Euler
Problem 45


Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.


author:  Adam Shechter
"""


def main():
    tri_list = triangonal_series(100000)
    pent_list = pentagonal_series(100000)
    hex_list = hexagonal_series(100000)
    print(tri_pent_hex_nums(tri_list, pent_list, hex_list))


def tri_pent_hex_nums(tri_list, pent_list, hex_list):
    answers = []
    for num in tri_list:
        print(".", end="")
        if num in  pent_list and num in hex_list:
            print("****** FOUND ********", num)
            answers.append(num)
    return answers


def triangonal_series(upper_limit):
    tri_list = []
    for i in range(1, upper_limit):
        tri_val = i * (i + 1) // 2
        tri_list.append(tri_val)
    return tri_list


def pentagonal_series(upper_limit):
    pent_list = []
    for i in range(1, upper_limit):
        pent_val = i * (3 * i - 1) // 2
        pent_list.append(pent_val)
    return pent_list


def hexagonal_series(upper_limit):
    hex_list = []
    for i in range(1, upper_limit):
        hex_val = i * (2 * i - 1)
        hex_list.append(hex_val)
    return hex_list


if __name__ == '__main__':
    main()
