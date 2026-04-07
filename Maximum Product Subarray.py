# Find the subarray in nums which has the largest product.
# Return the product.
# Return 0 if the array is empty.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # max_prod is the maximum so far
        # min_prod is the minimum so far
        # result is the final result
        max_prod = min_prod = result = nums[0]
        
        for end in nums[1:]:  # imagine the end
            # avoid overwriting min_prod by changing max_prod
            max_temp = max([end, max_prod * end, min_prod * end])

            # min_prod accounts for negative numbers
            min_prod = min([end, max_prod * end, min_prod * end])

            max_prod = max_temp
            result = max(max_prod, result)
        
        return result
        
