"""
Project Euler
Problem 17

If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

author:  Adam Shechter
"""

number_words = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand"
    }

def main():
    print(letters_in_number_series(1, 1000))


def letters_in_number_series(start, finish):
    word_sequence = ""
    for n in range(start, finish + 1):
        if n < 20:
            word_sequence += number_words[n] + " "
        elif 20 <= n < 100:
            dig1 = n % 10
            dig2 = n - dig1
            word_sequence += number_words[dig2] + " "
            word_sequence += number_words[dig1] + " "
        elif 100 <= n < 1000:
            dig1 = n % 10
            dig2 = (n - dig1) % 100
            dig3 = (n - dig2 - dig1) / 100
            word_sequence += number_words[dig3] + " " + number_words[100] + " "
            if 0 < (dig2+dig1) < 20:
                word_sequence += "and " + number_words[dig2+dig1] + " "
            elif 20 <= dig2 < 100:
                word_sequence += "and " + number_words[dig2] + " "
                word_sequence += number_words[dig1] + " "
        elif 1000 <= n:
            word_sequence += number_words[1] + " " + number_words[1000]
    print(word_sequence.replace(" ", ""))
    return len(word_sequence.replace(" ", ""))

if __name__ == '__main__':
    main()
