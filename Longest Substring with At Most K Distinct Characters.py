# Find the longest substring of s with at most k distinct characters.
# Return the length.
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}

        # low stores the frontmost character
        # ret stores the length to return
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i  # always stores rightmost place character appears
            if len(d) > k:
                low = min(d.values())  # low stores the frontmost character
                del d[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret
