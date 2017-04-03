"""
Project Euler
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words,
how many are triangle words?


author:  Adam Shechter
"""


def main():
    list_words = read_file_in_list("42_words.txt")
    print(list_words)
    list_len = sorted(map(lambda x: len(x), list_words), reverse=True)
    triangle_values = triangle_values_calc(list_len[0] * ltr_val('z'))
    print(triangle_value_word_count(list_words, triangle_values))


def triangle_value_word_count(words, tri_vals):
    count = 0
    for word in words:
        sum1 = word_val(word)
        if sum1 in tri_vals:
            count += 1
    return count


def triangle_values_calc(toprange):
    tri_vals =[]
    for n in range(1, toprange+1):
        tri_val = 0.5*n*(n+1)
        tri_vals.append(tri_val)
    return tri_vals


def word_val(word1):
    sum1 = 0
    for ltr in word1:
        sum1 += ltr_val(ltr)
    return sum1


def ltr_val(char1):
    return ord(char1) - 96


def read_file_in_list(filename):
    data = []
    with open(filename, "r") as f:
        data = f.read()
    data_out = [x.strip('"').strip().lower() for x in data.split(",")]
    return sorted(data_out)

if __name__ == '__main__':
    main()
