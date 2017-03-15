"""
Project Euler
Problem 18  - Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the  maximum total from top to bottom of the triangle below:



                            75
                          95 64
                        17 47 82
                      18 35 87 10
                    20 04 82 47 65
                  19 01 23 75 03 34
                88 02 77 73 07 63 67
              99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)


Solution
I'm using a brute force method with a recursive function to gather all possible sums, and return the greatest.
A better solution exists, possibly using dynamic programming.

author:  Adam Shechter
"""

TRI_INPUT1 = "3 7 4 2 4 6 8 5 9 3"
TRI_SIZE1 = 4

TRI_INPUT = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 " \
                 "99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 " \
                 "53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 " \
                 "14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 " \
                 "98 73 93 38 53 60 04 23"

TRI_SIZE = 15


def main():
    triangle_array = create_triangle(TRI_INPUT, TRI_SIZE)
    print(triangle_array)
    # print(max_path_sum(triangle_array, TRI_SIZE))
    print(max_path_sum_brute(triangle_array, TRI_SIZE))


def create_triangle(triangle_input, side_len):
    tri_split = [int(x) for x in triangle_input.strip().split()]
    triangle_arr = []
    tri_index = 0
    for i in range(1, side_len + 1):
        triangle_arr.append([])
        for j in range(i):
            triangle_arr[i-1].append(tri_split[tri_index])
            tri_index += 1
    return triangle_arr


def max_path_sum(tri_arr, side_len):
    location = [0, 0]
    sum_tri = 0
    for i in range(side_len-1):
        sum_tri += tri_arr[location[0]][location[1]]
        print(sum_tri, location,tri_arr[location[0]][location[1]])
        if tri_arr[location[0]+1][location[1]] > tri_arr[location[0]+1][location[1]+1]:
            location[0] += 1
        elif tri_arr[location[0]+1][location[1]] < tri_arr[location[0]+1][location[1]+1]:
            location[0] += 1
            location[1] += 1
        else:
            # if they're equal
            pass
    else:
        sum_tri += tri_arr[location[0]][location[1]]
        print(sum_tri, location, tri_arr[location[0]][location[1]])
    return sum_tri


def max_path_sum_brute(tri_arr, side_len):
    sum_list = []
    max_path_sum_recursive(tri_arr, side_len, sum_list)
    print(len(sum_list))
    print(sorted(sum_list))
    return max(sum_list)


def max_path_sum_recursive(tri_arr, side_len, sum_list, location=[0, 0], curr_sum=0):
    if location[0] == side_len - 1:
        curr_sum += tri_arr[location[0]][location[1]]
        sum_list.append(curr_sum)
        return
    else:
        curr_sum += tri_arr[location[0]][location[1]]
        max_path_sum_recursive(tri_arr, side_len, sum_list, [location[0]+1, location[1]], curr_sum)
        max_path_sum_recursive(tri_arr, side_len, sum_list, [location[0]+1, location[1]+1], curr_sum)

if __name__ == '__main__':
    main()
