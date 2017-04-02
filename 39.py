"""
Project Euler
Problem 39

Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?


SOLUTION:
a <= b < c

author:  Adam Shechter
"""


def main():
    print(max_integer_right_triangles(1000))


def max_integer_right_triangles(range2):
    max_solution = {"solutions": 0, "perimeter": 0}
    solutions_list = []
    for p in range(1, range2+1):
        # print("************** Perimeter {} ******************".format(p))
        solutions = integer_right_triangles(p)
        if solutions:
            solutions_list.append({"solutions": solutions, "perimeter": p})
        if solutions > max_solution['solutions']:
            max_solution['solutions'] = solutions
            max_solution['perimeter'] = p
    sort_solutions = sorted(solutions_list, key=lambda k: k['solutions'], reverse=True)
    print(sort_solutions)
    return max_solution


def integer_right_triangles(p):
    solutions = 0
    for a in range(1, (p // 3)+1):
        for b in range(p - a, (p//3) - 1, -1):
            c = p - a - b
            if not c:
                continue
            elif c < a or c < b:
                continue
            a2 = pow(a, 2)
            b2 = pow(b, 2)
            c2 = pow(c, 2)
            # print("a: {}    b: {}       c: {}".format(a,b,c))
            if a2 + b2 == c2:
                print("{}    *** FOUND ONE ***  a: {}    b: {}       c: {}".format(p, a,b,c))
                solutions += 1
    return solutions

if __name__ == '__main__':
    main()