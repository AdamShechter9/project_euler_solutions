"""
Project Euler
Problem 31

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

Solution
--------
Recursive
Start a recursive function trying all possible combinations.

Dynamic
Had to go online and do a little research.  This is based on the same approach
as the grid problem (#15) counting ways to get from top left to bottom right.


author:  Adam Shechter
"""


def main():
    target_sum = 200
    combinations = [1, 2, 5, 10, 20, 50, 100, 200]
    print(coin_call_dyn(target_sum, combinations))
    print(coin_call_rec(target_sum, combinations))


def coin_call_dyn(sum5, combinations):
    ways_map = [0] * (sum5 + 1)
    ways_map[0] = 1
    for coin_size in combinations:
        for i in range(coin_size, sum5+1):
            ways_map[i] += ways_map[i - coin_size]
    print("Dynamic: Solution for sum {} is {} combinations.".format(sum5, ways_map[sum5]))
    return ways_map[sum5]


def coin_call_rec(sum5, combinations):
    solutions = coin_recurs(sum5, combinations)
    print("Recursive: Solution for sum {} is {} combinations.".format(sum5, solutions))
    return solutions


def coin_recurs(n, combinations, score=0, coin=0):
    current_score = score + coin
    # Base cases
    if current_score > n:
        return 0
    elif current_score == n:
        return 1
    elif current_score < n:
        answer = 0
        for coin_size in combinations:
            if coin <= coin_size:
                answer += coin_recurs(n, combinations, current_score, coin_size)
    return answer

if __name__ == '__main__':
    main()
