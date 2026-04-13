'''
The idea is to find the number of turns it takes
to get to 1 using 3x + 1.

You sort the numbers from lo to hi inclusive
by that number in increasing order.
The secondary sort is by the numbers themselves, also increasing.

Then you find the kth value
where k = 1 indicates the first value.
'''
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # makes sure you don't constantly compute
        # the "power function" again and again
        # for the same values
        @cache
        def power(x):
            if x == 1:
                return 0
            elif x % 2 == 1:
                return 1 + power(3 * x + 1)
            return 1 + power(x // 2)
        
        # find the number and power function
        #
        collatz = [(num, power(num)) for num in range(lo, hi+1)]
        sorted_collatz = sorted(collatz, key=lambda x: (x[1], x[0]))
        
        return sorted_collatz[k-1][0]
        
