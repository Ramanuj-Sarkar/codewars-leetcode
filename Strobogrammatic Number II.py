# Find all numbers with n digits
# where the number would be read the same upside down
# 0 only counts as having 1 digit
# any other numbers can't start with 0
class Solution:
    digits_mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
    
    def findStrobogrammaticMiddle(self, n: int) -> List[int]:
        # base cases
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        
        # find acceptable middles
        middles = self.findStrobogrammaticMiddle(n-2)
        res = []
        
        # add the things to the sides
        for (digit, mapping) in self.digits_mapping.items():
            for middle in middles:
                res.append(digit + middle + mapping)
        
        return res
        
    def findStrobogrammatic(self, n: int) -> List[str]:
        # base cases
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        
        # find acceptable middles
        middles = self.findStrobogrammaticMiddle(n-2)
        res = []
        for (digit, mapping) in self.digits_mapping.items():
            # this is for acceptable final answers
            # they can't begin with 0
            if digit == '0':
                continue
            for middle in middles:
                res.append(digit + middle + mapping)
        
        return res
