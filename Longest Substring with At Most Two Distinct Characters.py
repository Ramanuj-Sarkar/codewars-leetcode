class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        cnt = {}
        ans = 0
        l = 0
        for r, x in enumerate(s):
            cnt[x] = cnt.get(x,0) + 1
            while len(cnt) > 2:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0: del cnt[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
        
