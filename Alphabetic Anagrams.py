from math import factorial
from functools import reduce

def list_position(word):
    """Return the anagram list position of the word"""
    if len(word) == 1:
        return 1
    unique_letters = sorted(set(word)) # remove duplicates and sort it
    count_letters = [word.count(l) for l in unique_letters]
    
    # Total number of possible combinations m!/(n! * (n-1)! * ...)
    total_combinations = factorial(len(word)) // reduce(lambda x,y: x * y, [factorial(c) for c in count_letters])

    # get the amount to increment
    increment = [0] + [c * total_combinations // len(word) for c in count_letters[:-1]]
    increment = [sum(increment[:i + 1]) for i in range(len(increment))]
    
    # recursively increment it correctly
    return increment[unique_letters.index(word[0])] + list_position(word[1:])
