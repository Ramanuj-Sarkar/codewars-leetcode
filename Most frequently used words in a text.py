from collections import defaultdict

# Find top 3 most used words in a text.
def top_3_words(text):
    text_dict = defaultdict(int)
    word = ''

    # catches all words and their frequencies
    for letter in text.lower():
        if ord('a') <= ord(letter) <= ord('z') or letter == "'":
            word += letter
        elif len(word) > 0 and any(ord('a') <= ord(l) <= ord('z') for l in word):
            text_dict[word] += 1
            word = ''
    
    # catches words at the end
    if len(word) > 0 and any(ord('a') <= ord(l) <= ord('z') for l in word):
        text_dict[word] += 1
        word = ''

    # return the top 3 words of the sorted dictionary
    return sorted(text_dict,key=(lambda x: -text_dict[x]))[:3]
