"""
Project Euler
Problem 48


The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


author:  Adam Shechter
"""


def main():
    print(increment_power_series(10))
    answer = increment_power_series(1000)
    print(answer)
    ans_str = str(answer)
    print("Answer (last 10 digits): {}".format(ans_str[-10:]))

def increment_power_series(limit):
    total_pow_sum = 0
    for n in range(1, limit+1):
        pow_product = pow(n, n)
        total_pow_sum += pow_product
        print("n = {}       product = {}        total = {}".format(n, pow_product, total_pow_sum))
    return total_pow_sum

if __name__ == '__main__':
    main()
