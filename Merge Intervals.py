# You have a list which is at least 1 interval long.
# The intervals are like [start, end], but some of them overlap.
# Merge the overlapping ones.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort them so the overlapping ones are near each other
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        
        answer = []
        
        # the first and second values of the first interval
        prev_first, prev_second = sorted_intervals[0]
        
        for first, second in sorted_intervals[1:]:
            if first <= prev_second:  # overlapping
                prev_second = max(second, prev_second)
            else:  # not overlapping
                answer.append([prev_first, prev_second])
                prev_first, prev_second = first, second
        
        # You also need to return the last one
        return answer + [[prev_first, prev_second]]
