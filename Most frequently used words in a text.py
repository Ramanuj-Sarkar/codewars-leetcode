from collections import defaultdict
def top_3_words(text):
    text_dict = defaultdict(int)
    word = ''
    for letter in text.lower():
        if ord('a') <= ord(letter) <= ord('z') or letter == "'":
            word += letter
        elif len(word) > 0 and any(ord('a') <= ord(l) <= ord('z') for l in word):
            text_dict[word] += 1
            word = ''
    if len(word) > 0 and any(ord('a') <= ord(l) <= ord('z') for l in word):
        text_dict[word] += 1
        word = ''
    return sorted(text_dict,key=(lambda x: -text_dict[x]))[:3]
