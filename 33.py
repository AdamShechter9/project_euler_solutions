"""
Project Euler
Problem 3

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting
to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

author:  Adam Shechter
"""
from decimal import *
from functools import reduce
getcontext().prec = 6


def main():
    fractions = digit_cancelling_fractions()
    print(fractions)
    fractions2 = [Decimal(x[2]) for x in fractions]
    decimal1 = Decimal(str(reduce(lambda x, y: x * y, fractions2)))
    print(decimal1.as_integer_ratio())


def digit_cancelling_fractions():
    answers = []
    for numerator in range(10, 99):
        for denominator in range(10, 99):
            if numerator == denominator:
                continue
            else:
                fraction = numerator / denominator
                numS = str(numerator)
                denS = str(denominator)
                if numS[-1:] == '0' and denS[-1:] == '0':
                    continue
                elif fraction >= 1:
                    continue
                else:
                    if numS[:1] == denS[:1]:
                        num2 = int(numS[1:])
                        den2 = int(denS[1:])
                        try:
                            fraction2 = num2 / den2
                            if fraction2 == fraction:
                                answers.append([numerator, denominator, fraction])
                        except ZeroDivisionError:
                            continue
                    if numS[:1] == denS[1:]:
                        num2 = int(numS[1:])
                        den2 = int(denS[:1])
                        try:
                            fraction2 = num2 / den2
                            if fraction2 == fraction:
                                answers.append([numerator, denominator, fraction])
                        except ZeroDivisionError:
                            continue

                    if numS[1:] == denS[1:]:
                        num2 = int(numS[:1])
                        den2 = int(denS[:1])
                        try:
                            fraction2 = num2 / den2
                            if fraction2 == fraction:
                                answers.append([numerator, denominator, fraction])
                        except ZeroDivisionError:
                            continue

                    if numS[1:] == denS[:1]:
                        num2 = int(numS[:1])
                        den2 = int(denS[1:])
                        try:
                            fraction2 = num2 / den2
                            if fraction2 == fraction:
                                answers.append([numerator, denominator, fraction])
                        except ZeroDivisionError:
                            continue

    return answers

if __name__ == '__main__':
    main()