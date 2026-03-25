class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minsum = nums[0] + nums[1] + nums[2]

        sortnums = sorted(nums)

        for x in range(len(sortnums)):
            left = x + 1
            right = len(sortnums) - 1
            while left < right:
                newsum = sortnums[x] + sortnums[left] + sortnums[right]
                if newsum == target:
                    return newsum
                elif abs(target - newsum) < abs(target - minsum):
                    minsum = newsum
                
                if newsum < target:
                    left += 1
                else:
                    right -= 1
        return minsum
