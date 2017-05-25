"""
Project Euler
Problem 58

Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal,
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime;
that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above,
a square spiral with side length 9 will be formed.
If this process is continued,
what is the side length of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?


SOLUTION:
Tried with brute force first, by creating a number matrix and calculating prime ratios.
Since it's a slow unoptimized solution (Once them matrix has sides greater than 3000 it slows down),

I went ahead and dynamically generated the number series through math and run prime ratio calculation.

author:  Adam Shechter
"""
import math


def main():
    grid_size = 7
    while 1:
        current_ratio = diagonal_number_series(grid_size)
        print("*" * 50)
        print("side length: {}      ratio primes:  {:.3%}".format(grid_size, current_ratio))
        if current_ratio < 0.1:
            break
        else:
            grid_size += 2


def diagonal_number_series(side_length):
    number_series = [1, 3, 5, 7, 9]
    max_num = ((side_length - 1) / 2) * 4 + 1
    increment = 8
    index = 0
    while len(number_series) < max_num:
        index += 1
        increment += 2
        number_series.append(number_series[index]+increment)
    # print(number_series)
    prime_count = 0
    for num in number_series:
        if is_prime(num):
            prime_count += 1
    return prime_count / len(number_series)


def is_prime(n):
    # 1 is not a prime
    if n == 1:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    else:
        for i in range(11, math.floor(pow(n, 0.5))+2, 2):
            if n % i == 0:
                return False
    return True


# DEPRECATED
# NOT USED
def ratio_primes_diagonals(matrix):
    diagonals_nums = set()
    maxn = len(matrix)
    for col in range(maxn):
        diagonals_nums.add(matrix[col][col])
        diagonals_nums.add(matrix[col][maxn-1-col])
    prime_count = 0
    for num in diagonals_nums:
        if is_prime(num):
            prime_count += 1
    return prime_count / len(diagonals_nums)


# DEPRECATED
# NOT USED
def create_number_spiral(grid_size):
    if grid_size % 2 == 0 or grid_size < 1:
        return "Error.  Must be odd number"
    # Create Matrix
    matrix = []
    for row in range(grid_size):
        matrix.append([])
        for col in range(grid_size):
            matrix[row].append(0)
    # first row
    current_grid_size = grid_size
    rev_counter = grid_size * grid_size + 1
    location = [grid_size - 1, grid_size]
    # left
    for i in range(current_grid_size):
        rev_counter -= 1
        location[1] -= 1
        matrix[location[0]][location[1]] = rev_counter
    direction = "up"
    while current_grid_size > 1:
        current_grid_size -= 1
        if direction == "down":
            # down
            for j in range(current_grid_size):
                matrix[location[0]][location[1]] = rev_counter
                rev_counter -= 1
                location[0] += 1
            # left
            for m in range(current_grid_size):
                matrix[location[0]][location[1]] = rev_counter
                rev_counter -= 1
                location[1] -= 1
            direction = "up"
        elif direction == "up":
            # up
            for l in range(current_grid_size):
                matrix[location[0]][location[1]] = rev_counter
                rev_counter -= 1
                location[0] -= 1
            # right
            for k in range(current_grid_size):
                matrix[location[0]][location[1]] = rev_counter
                rev_counter -= 1
                location[1] += 1
            direction = "down"
    matrix[location[0]][location[1]] = rev_counter
    return matrix


if __name__ == '__main__':
    main()