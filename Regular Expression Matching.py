class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = len(s) - 1, len(p) - 1
        return self.backtrack({}, s, p, i, j)

    def backtrack(self, cache, s, p, i, j):
        # return value if it was already seen
        key = (i, j)
        if key in cache:
            return cache[key]

        # empty string is true
        if i == -1 and j == -1:
            cache[key] = True
            return True

        # p reached beginning and s did not
        if i != -1 and j == -1:
            cache[key] = False
            return cache[key]

        # * is zero or more so there can be
        # zero characters before *
        if i == -1 and p[j] == '*':
            k = j
            while k != -1 and p[k] == '*':
                k -= 2
            
            if k == -1:
                cache[key] = True
                return cache[key]
            
            cache[key] = False
            return cache[key]
        
        # we reached the beginning of s
        # but not p, and there's no excuse
        if i == -1 and p[j] != '*':
            cache[key] = False
            return cache[key]

        if p[j] == '*':
            # again, because of the zero characters thing
            if self.backtrack(cache, s, p, i, j - 2):
                cache[key] = True
                return cache[key]
            
            # .* can account for all the subsequent characters
            if p[j - 1] == s[i] or p[j - 1] == '.':
                if self.backtrack(cache, s, p, i - 1, j):
                    cache[key] = True
                    return cache[key]
        
        # checks whether the values are equal
        if p[j] == '.' or s[i] == p[j]:
            if self.backtrack(cache, s, p, i - 1, j - 1):
                cache[key] = True
                return cache[key]

        cache[key] = False
        return cache[key]
