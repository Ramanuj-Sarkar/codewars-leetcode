# You have a list of words of the same length.
# You have to figure out which groups of words create word squares
# where the nth word read horizontally is the same as the nth word read vertically
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # length of all words
        n = len(words[0])

        # prefixes of words
        prefixes = defaultdict(list)
        
        for word in words:
            for i in range(n):
                # words corresponding to prefixes
                prefixes[word[:i]].append(word)
        
        squares = []

        def build(square):
            if len(square) == n:
                # returns with finished square
                squares.append(square)
            else:
                # zip(*square) puts all the 1st, 2nd, etc. letters together
                # list() makes it subscriptable
                # len(square) finds the bottom / rightmost group of characters
                # ''.join() joins them into a single prefix
                for word in prefixes[''.join(list(zip(*square))[len(square)])]:
                    build(square + [word])
        
        for word in words:
            build([word])
        
        return squares
