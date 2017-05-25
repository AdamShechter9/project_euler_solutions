"""
Project Euler
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

author:  Adam Shechter
"""


def main():
    matrix = create_number_spiral(1001)
    print(matrix)
    print(sum_diagonals(matrix, 1001))


def sum_diagonals(matrix, grid_size):
    sum_diag = 0
    for i in range(grid_size // 2):
        sum_diag += matrix[i][i]
        sum_diag += matrix[grid_size - 1 - i][i]
        sum_diag += matrix[i][grid_size - 1 - i]
        sum_diag += matrix[grid_size - 1 - i][grid_size - 1 - i]
    else:
        sum_diag += 1
    return sum_diag

def create_number_spiral(grid_size):
    if grid_size % 2 == 0 or grid_size < 1:
        return "Error.  Must be odd number"
    matrix = []
    for row in range(grid_size):
        matrix.append([])
        for col in range(grid_size):
            matrix[row].append(0)
    # first row
    current_grid_size = grid_size
    rev_counter = grid_size * grid_size + 1
    location = [0, grid_size]
    for i in range(current_grid_size):
        rev_counter -= 1
        location[1] -= 1
        matrix[location[0]][location[1]] = rev_counter
    direction = "down"

    while current_grid_size > 1:
        # print(matrix)
        # print(location, rev_counter, direction)
        current_grid_size -= 1
        if direction == "down":
            # down
            for j in range(current_grid_size):
                matrix[location[0]][location[1]] = rev_counter
                rev_counter -= 1
                location[0] += 1
            # right
            for k in range(current_grid_size):
                matrix[location[0]][location[1]] = rev_counter
                rev_counter -= 1
                location[1] += 1
            direction = "up"
        elif direction == "up":
            # up
            for l in range(current_grid_size):
                matrix[location[0]][location[1]] = rev_counter
                rev_counter -= 1
                location[0] -= 1
            # left
            for m in range(current_grid_size):
                matrix[location[0]][location[1]] = rev_counter
                rev_counter -= 1
                location[1] -= 1
            direction = "down"
    matrix[location[0]][location[1]] = rev_counter
    return matrix

if __name__ == '__main__':
    main()