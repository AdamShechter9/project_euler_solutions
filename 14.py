"""
Project Euler
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


Solution:
Using memoization and greedy to speed up calculation.


author:  Adam Shechter
"""


def main():
    print(max_collatz_seq(1000000))


def max_collatz_seq(n):
    result_map = {}
    max_s = 0
    num = 0
    for j in range(1, n+1):
        count = 1
        k = j
        while k != 1:
            if k in result_map.keys():
                count += result_map[k] - 1
                break
            else:
                k = seq_func(k)
                count += 1
        result_map[j] = count
        if count > max_s:
            max_s = count
            num = j
    print(result_map)
    return num, max_s


def seq_func(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n+1

if __name__ == '__main__':
    main()
