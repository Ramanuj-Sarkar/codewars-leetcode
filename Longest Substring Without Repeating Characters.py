class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        subs = ''
        
        for x in s:
            if x not in subs:
                subs += x
                n = max(len(subs), n)
            else:
                subs = subs[subs.index(x)+1:] + x
        
        return n
