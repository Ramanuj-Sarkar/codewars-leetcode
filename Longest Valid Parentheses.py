'''
Given a string containing just the characters '(' and ')',
return the length of the longest valid (well-formed) parentheses substring.

If there is none, return 0.
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # stack[0] is a value that no valid parentheses substring can pass
        # the other values in stack correspond to open parentheses
        # this allows for simpler code
        stack = [-1]
        
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack):
                    # len(stack) > 0
                    max_len = max(max_len, i - stack[-1])
                else:
                    # no valid parentheses substring can pass this many ')'s
                    stack.append(i)
        
        return max_len
