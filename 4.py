"""
Project Euler
Problem 5

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Solution
Start backwards from 999 x 999 down to 999 x 100 looking for palindromes.
Add any finds to list.
Decrement by one, and repeat with 998 x 998 down to 998 x 100.
add any finds to list.
go all the way down to 100 x 100.
take max of palindrome list result.

author:  Adam Shechter
"""


def main():
    print(largest_palindrome(3))


def largest_palindrome(digits):
    print("Provided {} digits".format(digits))
    palindromes = []
    multiplier = int("1"*digits)
    a_max = multiplier * 9
    a_min = a_max // 10
    for i in range(a_max, a_min, -1):
        for j in range(a_max, a_min, -1):
            product = i * j
            if is_palindrome(product):
                palindromes.append(product)
    print("Palindromes\n", palindromes)
    return max(palindromes)


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