# Divide two integers without using multiplication, division, and modulo
# This integer division should truncate towards 0
# If the quotient is strictly greater than 2^(31) - 1, then return 2^(31) - 1
# If the quotient is strictly less than -2^(31), then return -2^(31)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # get rid of edge cases
        if dividend == divisor:
            return 1
        if dividend == -2**31 and divisor == -1:
            return (2**31) - 1
        if divisor == 1:
            return dividend
        
        # find sign
        sign = -1 if (dividend < 0) != (divisor < 0) else 1

        # get clean divisors
        n, d = abs(dividend), abs(divisor)
        
        # final answer
        ans = 0

        while n >= d:
            p = 0
            
            # you find the thing you use to multiply d
            # by repeatedly multiplying d by 2 in a sense
            while n >= (d << (p + 1)):
                p += 1
            
            # you subtract this from n
            n -= (d << p)

            # you essentially multiplied d by this 1 << p
            # to get d << p
            ans += (1 << p)
        
        return min(max(sign * ans, -2**31), 2**31 - 1)
