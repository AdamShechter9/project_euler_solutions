"""
Project Euler
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total sum of all the name scores in the file?

author:  Adam Shechter
"""


def main():
    name_list = load_sort_names()
    print(total_sum_name_score(name_list))


def total_sum_name_score(name_list):
    score_list = []
    for i in range(len(name_list)):
        score = (i+1) * sum([ord(c)-64 for c in name_list[i]])
        score_list.append(score)
    return sum(score_list)


def load_sort_names():
    with open("22_names.txt", "r") as f:
        names = f.read().split(",")
    for i in range(len(names)):
        names[i] = names[i].strip('"')
    return sorted(names)

if __name__ == '__main__':
    main()