"""
Project Euler
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

Solution:
Brute Force:
Use a recursive solution to map out all possible paths and return count.
This gives the correct answer, but performs poorly with larger grids.

After a little research, I realized dynamic programming solution could be applied.


author:  Adam Shechter
"""


def main():
    print(find_paths_dynprog(20))
    # print(possible_paths_grid_rec(20))


def construct_grid(grid_size):
    grid = []
    for row in range(grid_size + 1):
        grid.append([])
        for col in range(grid_size + 1):
            grid[row].append("*")
    print(grid)
    return grid


def find_paths_dynprog(grid_size):
    grid = construct_grid(grid_size)
    # set outside boundary
    for i in range(grid_size+1):
        grid[grid_size][i] = 1
        grid[i][grid_size] = 1
    grid[grid_size][grid_size] = 0
    # calculate paths going backwards
    for row in range(grid_size+1):
        for col in range(grid_size+1):
            if grid[grid_size-row][grid_size-col] == "*":
                grid[grid_size - row][grid_size - col] = grid[grid_size - row+1][grid_size - col] + grid[grid_size - row][grid_size - col+1]
            else:
                pass
    print(grid)
    return grid[0][0]


def possible_paths_grid_rec(grid_size):
    grid = construct_grid(grid_size)
    count = [0]
    find_paths_rec(grid, count)
    return count


def find_paths_rec(grid, count, location=[0, 0]):
    x = location[0]
    y = location[1]
    # Base case
    if location[0] == (len(grid) - 1) and location[1] == (len(grid) - 1):
        count[0] += 1
        print(count[0])
        return
    elif location[0] == (len(grid) - 1):
        find_paths_rec(grid, count, [x, y + 1])
    elif location[1] == (len(grid) - 1):
        find_paths_rec(grid, count, [x + 1, y])
    else:
        find_paths_rec(grid, count, [x + 1, y])
        find_paths_rec(grid, count, [x, y + 1])


if __name__ == '__main__':
    main()
