"""
Project Euler
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


SOLUTION
Brute force solution would have you increment a number and test for even divisions.
We know a few things about the number we're looking for.
It's an even number (we can increment with step of 2, not one).
it's greater than 2520.

We only need to test the following numbers (factors in parentheses):
20 (2, 5, 10),
19
18 (2, 3, 9)
17
16 (2, 4, 8)
15 (3, 5)
14 (2, 7)
13
12 (2, 3, 6)
11

Don't need to test:
10, 9, 8, 7, 6, 5, 4, 3, 2

author:  Adam Shechter
"""


def main():
    print(smallest_multiple(11, 20))


def smallest_multiple(minx, maxx):
    test_x = maxx
    while True:
        for i in range(maxx, minx-1, -1):
            if test_x % i != 0:
                break
        else:
            return test_x
        test_x += 2

if __name__ == '__main__':
    main()