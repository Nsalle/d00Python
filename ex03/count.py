import sys
import string


def text_analyzer(*args):
    if len(args) > 1:
        print("ERROR")
        exit()
    if len(args) == 0:
        strin = input("What is the text to analyse?\n")
    else:
        strin = args[0]
    print("-", sum(1 for c in strin if c.isupper()), "upper letters")
    print("-", sum(1 for c in strin if c.islower()), "lower letters")
    nbpunct = 0
    for c in strin:
        if c in string.punctuation:
            nbpunct += 1
    print("-", nbpunct, "punctuation marks")
    print("-", sum(1 for c in strin if c.isspace()), "spaces")
