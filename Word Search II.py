# This data structure makes it easier to do stuff
class Trie:

    def __init__(self):
        self.root = {}
        
    # lets you insert word into trie
    def insert(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        
        curr['end'] = True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        trie = Trie()

        # insert all the words
        for w in words:
            trie.insert(w)

        rows = len(board)
        cols = len(board[0])
        
        def search(b, r, x, y, path):
            # you've already seen this word
            if 'end' in r:
                ans.append(path)
                del r['end']
            
            # it is too big in this case
            if not (0 <= x < rows and 0 <= y < cols):
                return
            
            # you need to save this value
            temp = b[x][y]

            if temp not in r:
                return
            
            # now we see if we get more words by adding this value
            r = r[temp]
            
            # this is not a letter
            # so we don't double-dip
            b[x][y] = 'not'

            # we find the letters around it
            search(b, r, x+1, y, path + temp)
            search(b, r, x-1, y, path + temp)
            search(b, r, x, y+1, path + temp)
            search(b, r, x, y-1, path + temp)

            # we set it back now
            b[x][y] = temp
        
        for i in range(rows):
            for j in range(cols):
                search(board, trie.root, i, j, '')
    
        return ans
