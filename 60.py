"""
Project Euler
Problem 1

The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result will always be prime.

For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

author:  Adam Shechter
"""
from prime_list import prime_list

primes = prime_list.PrimeNums()

# Using memoization for optimization
invalid_primes = {}


def main():
    prime_pair_sets(50000)


def prime_pair_sets(limit_n):

    for i1 in range(len(primes.primes)):
        if primes.primes[i1] > limit_n:
            break
        n1 = primes.primes[i1]
        for i2 in range(i1+1, len(primes.primes)):
            if primes.primes[i2] > limit_n:
                break
            n2 = primes.primes[i2]
            try:
                if n2 in invalid_primes[n1]:
                    continue
            except KeyError:
                pass
            # print(invalid_primes)
            for i3 in range(i2+1, len(primes.primes)):
                if primes.primes[i3] > limit_n:
                    break
                n3 = primes.primes[i3]
                try:
                    if n3 in invalid_primes[n2]:
                        continue
                except KeyError:
                    pass
                for i4 in range(i3+1, len(primes.primes)):
                    if primes.primes[i4] > limit_n:
                        break
                    n4 = primes.primes[i4]
                    try:
                        if n4 in invalid_primes[n3]:
                            continue
                    except KeyError:
                        pass
                    for i5 in range(i4+1, len(primes.primes)):
                        if primes.primes[i5] > limit_n:
                            break
                        n5 = primes.primes[i5]
                        try:
                            if n5 in invalid_primes[n4]:
                                continue
                        except KeyError:
                            pass
                        print('TESTING: {} {} {} {} {}'.format(n1, n2, n3, n4, n5))
                        if test_prime_set([n1, n2, n3, n4, n5]):
                            print("FOUND!!!!")
                            print("{} {} {} {} {}".format(n1, n2, n3, n4, n5))
                            print("sum: {} ".format(sum([n1, n2, n3, n4, n5])))
                            return True
    print("Limit exceeded.  Terminating process.")
    return False


# testing concatenation results are prime
def test_prime_set(test_set):
    pass_test = True
    for i1 in range(len(test_set)):
        n1 = test_set[i1]
        for i2 in range(i1+1, len(test_set)):
            n2 = test_set[i2]
            if not test_primes(n1, n2):
                try:
                    if n2 not in invalid_primes[n1]:
                        invalid_primes[n1].append(n2)
                except:
                    invalid_primes[n1] = [n2]
                pass_test = False
    return pass_test


def test_primes(n1, n2):
    test1 = str(n1) + str(n2)
    test2 = str(n2) + str(n1)
    # print('{} {}    {} {}'.format(n1, n2, test1, test2))
    if primes.is_prime(int(test1)) and primes.is_prime(int(test2)):
        return True
    else:
        return False

if __name__ == '__main__':
    main()
