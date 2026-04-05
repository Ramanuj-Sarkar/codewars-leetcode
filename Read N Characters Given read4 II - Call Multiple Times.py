# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.to_load = collections.deque() # this is used to analyze data in buf4
    
    def read(self, buf: List[str], n: int) -> int:
        read_count = 0
        buf4 = ['']*4 
        while read_count < n: # main logic: read until arrive at n
            if len(self.to_load) > 0: # load from buffer to buf
                buf[read_count] = self.to_load.popleft() # O(1)
                read_count += 1
            else: # load file to buf4
                for i in range(read4(buf4)):
                    self.to_load.append(buf4[i])
                if len(self.to_load) == 0: # edge case, nothing to load
                    break
        return read_count
