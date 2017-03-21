"""
Project Euler
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known
that the greatest number that cannot be expressed as the sum of two abundant
numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


SOLUTION
Find all abundant numbers and add to a list.


author:  Adam Shechter
"""


def main():
    # abundant_nums = abundant_nums_list(1000)
    abundant_nums = abundant_nums_list(28123)
    print(abundant_nums)
    print(sum_pos_int_not_abundant(abundant_nums, 28123))


def sum_pos_int_not_abundant(abundant_nums, upper_range):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    for i in range(24, upper_range+1):
        if (i / 2) in abundant_nums:
            pass
        else:
            found = False
            for abund_num in abundant_nums:
                x = i - abund_num
                if x in abundant_nums:
                    print("{} = {} + {}".format(i, x, abund_num))
                    break
                if abund_num > i:
                    found = True
                    break
            if found:
                print("********* FOUND Adding {}".format(i))
                num_list.append(i)
    return sum(num_list)


def abundant_nums_list(upper_range):
    abundant_nums = []
    for i in range(3, upper_range+1):
        factors_sum = sum(find_factors(i))
        if factors_sum > i:
            print(i)
            abundant_nums.append(i)
    return abundant_nums


def find_factors(n):
    factors = []
    i = 1
    while i <= (n // 2 + 1):
        if n % i == 0:
            if i not in factors:
                factors.append(i)
            if (n // i) not in factors and (n // i) < n:
                factors.append((n // i))
        i += 1
    return factors

if __name__ == '__main__':
    main()