# The integer array nums contains numbers
# if nums[i] == nums[j] == nums[k], the tuple is good
# if there are no good tuples, return -1
# else, return the minimum possible distance of a good tuple
# the distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i)
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        # contains next index of nums[i]
        # or -1 if there is none
        next_occurrence = [-1] * n
        # records most recent occurrence of nums[i]
        most_recent_occurrence = {}
        # stores minimum distance
        answer = n + 1

        for i in range(n - 1, -1, -1):
            # updates next index for this value
            if nums[i] in most_recent_occurrence:
                next_occurrence[i] = most_recent_occurrence[nums[i]]
            # updates recent index
            most_recent_occurrence[nums[i]] = i

        # find second and third value
        # by repeatedly looking at next value
        for i in range(n):
            second_pos = next_occurrence[i]
            if second_pos != -1:
                third_pos = next_occurrence[second_pos]
                if third_pos != -1:
                    answer = min(answer, third_pos - i)

        # multiply answer by 2 because
        # abs(i - j) + abs(j - k) + abs(k - i)
        # always equals 2 * abs(k - i)
        return -1 if answer == n + 1 else answer * 2
  
