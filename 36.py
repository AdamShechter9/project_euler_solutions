"""
Project Euler
Problem 36

Double base palindromes

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)


author:  Adam Shechter
"""


def main():
    dbl_base_palinds = dbl_base_palindromes(1000000)
    print(dbl_base_palinds)
    print(sum([x[0] for x in dbl_base_palinds]))


def dbl_base_palindromes(range1):
    answers = []
    for n in range(1, range1):
        base10palind = is_palindrome(str(n))
        base2palind = is_palindrome("{:b}".format(n))
        if base10palind and base2palind:
            answers.append([n, "{:b}".format(n)])
    return answers


def is_palindrome(x):
    x_str = str(x)
    half_len = len(x_str) // 2
    if len(x_str) % 2 == 0:
        x_str2 = x_str[half_len:]
    else:
        x_str2 = x_str[(half_len+1):]
    x_str2 = x_str2[::-1]
    return x_str[:half_len] == x_str2

if __name__ == '__main__':
    main()
