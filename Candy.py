# People have been given hunger values in ratings.
# Each person must have at least one candy.
# People with higher ratings get more than their neighbors.
# Return the minimum number of candies you have to distribute.
# Return 0 for an empty list (no people).
class Solution:
    def candy(self, ratings: List[int]) -> int:

        if len(ratings) == 0:
            return 0
        
        candies = 1
        peak = up = down = 0

        for i in range(1, len(ratings)):
            if ratings[i - 1] > ratings[i]:
                # increasing
                up = 0
                down += 1
                candies += down + 1 - (1 if peak >= down else 0)
            elif ratings[i - 1] < ratings[i]:
                # decreasing
                up += 1
                peak = up
                down = 0
                candies += up + 1
            else:
                # flat_slope
                peak = up = down = 0
                candies += 1

        return candies
