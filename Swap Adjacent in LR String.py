'''
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL"
a move consists of either replacing one occurrence of "XL" with "LX",
or replacing one occurrence of "RX" with "XR".

Given the starting string start and the ending string result,
return True if and only if there exists a sequence of moves to transform start to result.
'''
class Solution:
	
    '''
    1. L and R can't cross one another, so the order has to stay the same.
    2. R can only cross to the right, so start_index <= final_index
    3. L can only cross to the left, so start_index >= final_index
    '''
    def canTransform(self, start: str, end: str) -> bool:
        '''
        Check if the order is the same.
        '''
        if start.replace("X", "") != end.replace("X", ""):
            return False
        
        '''
        Check condition 2.
        '''
        start_R = [num for num, r in enumerate(start) if r == "R"]
        end_R = [num for num, r in enumerate(end) if r == "R"]
        
        for start_index, final_index in zip(start_R, end_R):
            if start_index > final_index:
                return False
        
        '''
        Check condition 3.
        '''
        start_L = [num for num, l in enumerate(start) if l == "L"]
        end_L = [num for num, l in enumerate(end) if l == "L"]
        
        for start_index, final_index in zip(start_L, end_L):
            if start_index < final_index:
                return False
        
        return True
