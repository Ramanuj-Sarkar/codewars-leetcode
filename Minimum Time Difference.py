'''
Given a list of 24-hour clock time points in "HH:MM" format,
return the minimum minutes difference between any two time-points in the list. 

The times can wrap around
i.e. one time can be "late this night"
and the other can be "early tomorrow morning".
'''
class Solution:
    def findMinDifference(self, time_points: List[str]) -> int:
        points = set()
        for time in time_points:
            # create actual integer
            time_num = int(time[:2]) * 60 + int(time[3:])

            if time_num in points:
                return 0  # this means the times are the same
            
            points.add(time_num)
            # to make sure the times can wrap around
            if time_num < 720:
                points.add(time_num + 1440)
        
        # sort values
        sortp = sorted(points)

        # return minimum
        return min(sortp[x] - sortp[x-1] for x in range(1, len(sortp)))
