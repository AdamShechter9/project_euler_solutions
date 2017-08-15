"""
Adam Shechter Aug 2017

Prime List Module

reads prime numbers list into a memory variable.

Checks to see if number is prime.
"""


class PrimeNums(object):
    def __init__(self):
        self.primes = []
        self.primes = self._readprimes()

    def _readprimes(self):
        prime_nums = []
        try:
            with open('./prime_list/prime_list.txt') as f:
                prime_nums = [int(x) for x in f.read().strip().split()]
        except IOError:
            print('ERROR!  File Error.')
        return prime_nums

    def is_prime(self, x):
        if x in self.primes:
            return True
        else:
            return False

if __name__ == '__main__':
    print("ERROR.  This is a python module")
