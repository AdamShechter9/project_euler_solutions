"""
Project Euler
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.


author:  Adam Shechter
"""


def main():
    print(sum_multiples())


def sum_multiples(multiples=[3,5], low_range=0, up_range=1000):
    sum1 = 0
    for n in range(low_range, up_range):
        for mult in multiples:
            if n % mult == 0:
                sum1 += n
                break
    return sum1

if __name__ == '__main__':
    main()
