# You have a list which is at least 1 interval long.
# The intervals are like [start, end], but some of them overlap.
# You also have to add a new interval which might overlap with some.
# Merge the overlapping ones.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # add the new interval and sort this
        intervals = sorted(intervals + [newInterval])

        answer = []
        prev_first, prev_second = intervals[0]

        for first, second in intervals[1:]:
            if prev_second >= first:  # overlapping
                prev_second = max(prev_second, second)
            else:  # not overlapping
                answer.append([prev_first, prev_second])
                prev_first, prev_second = first, second
        
        # remember to include the last interval
        return answer + [[prev_first, prev_second]]
