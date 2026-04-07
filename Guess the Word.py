'''

You have an rray of unique strings words where words[i] is six letters long.
The helper object Master can run Master.guess(word) and returns
-1 if word is not from words.
Otherwise, it returns an integer
representing the number of exact matches (value and position)
of your guess to the secret word.

There is a parameter allowedGuesses
for each test case where allowedGuesses is the maximum number of times
you can call Master.guess(word).

For each test case, you should call Master.guess
with the secret word without exceeding
the maximum number of allowed guesses. 

# """
# This is Master's API interface.
# """
# class Master:
#     def guess(self, word: str) -> int:
'''
class Solution:
    def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
        # finds Counter of first letters, Counter of second letters, etc.
        # e.g. if wordlist = ["xy", "ab", "xz"]
        # then weights = [{x: 2, a: 1}, {b: 1, y:1, z:1}]
        weights = [Counter(word[i] for word in wordlist) for i in range(6)]

        # sort wordlist, least similar to rest of corpus first
        # they are least similar because Counter has smaller numbers for them
        wordlist.sort(key=lambda word: sum(weights[i][c] for i, c in enumerate(word)))

        while wordlist:
            # get the word most similar to the rest of the corpus
            # by popping from the *end* of wordlist
            word = wordlist.pop()
            matches = master.guess(word)

            if matches == 6:
                break  # we found the word early

            # only those words that share exactly x characters with word
            # can be the solution.
            wordlist = [
                other
                for other in wordlist
                if matches == sum(w == o for w, o in zip(word, other))
            ]
       
