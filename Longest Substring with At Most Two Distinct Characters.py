# Find the longest substring of s with at most k distinct characters.
# Return the length.
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        cnt = {}
        ans = 0  # answer
        l = 0  # frontmost character
        for r, x in enumerate(s):
            cnt[x] = cnt.get(x,0) + 1
            while len(cnt) > 2: # move l rightwards until the third one is gone
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0: del cnt[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
        
