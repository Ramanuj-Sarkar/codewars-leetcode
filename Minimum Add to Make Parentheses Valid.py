class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # you are adding parentheses
        # any part of the string
        # always the same kind of parentheses

        # ( = 1
        # ) = -1
        number_close = 0
        stack = []

        for char in s:
            if char == ')':
                if len(stack) == 0:
                    number_close += 1
                else:
                    stack.pop()
            else:
                stack.append('(')
        
        return len(stack) + number_close
        
