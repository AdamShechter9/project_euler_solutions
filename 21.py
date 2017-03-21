"""
Project Euler
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b,
then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


SOLUTION
Compile a list of a all amicable pairs, and print out the sum.


author:  Adam Shechter
"""


def main():
    pairs = amicable_pairs(10000)
    print(pairs)
    print(sum(pairs))


def amicable_pairs(top_range):
    pairs = []

    for i in range(1, top_range+1):
        fac_sum = sum(find_factors(i))
        fac_sum2 = sum(find_factors(fac_sum))
        print("a: {}    d(a)=b: {}    d(b)=a: {} ".format(i, fac_sum, fac_sum2))
        if fac_sum2 == i and fac_sum not in pairs and fac_sum != i:
            pairs.append(i)
            pairs.append(fac_sum)
            print("******* FOUND ********")
    return pairs


def find_factors(n):
    factors = []
    i = 1
    while i <= (n//2+1):
        if n % i == 0:
            if i not in factors:
                factors.append(i)
            if (n//i) not in factors and (n//i) < n:
                factors.append((n//i))
        i += 1
    return factors

if __name__ == '__main__':
    main()
