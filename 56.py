"""
Project Euler
Problem 56

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?


author:  Adam Shechter
"""


def main():
    print(greatestdigitsum(100, 100))


def greatestdigitsum(a, b):
    summax = 0
    x = 1
    y = 1
    while x < a and y < b:
        num = pow(x, y)
        digsum = digitsum(num)
        print(x,y, num, digsum)
        if digsum > summax:
            summax = digsum
        x += 1
        if x == a:
            x = 1
            y += 1
    return summax

# Two ways to go about this:
# One, you convert to string and add all digits converted back to int, one by one.
# Two, you mod10 and add to sum one by one.
def digitsum(n):
    x = n
    sumdig = 0
    while x != 0:
        sumdig += x % 10
        x //= 10
    return sumdig

if __name__ == '__main__':
    main()
