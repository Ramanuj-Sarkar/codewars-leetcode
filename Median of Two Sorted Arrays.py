class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
            
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            partX = (low + high) // 2
            partY = (x + y + 1) // 2 - partX
            
            maxlX = float('-inf') if partX == 0 else nums1[partX - 1]
            minrX = float('inf') if partX == x else nums1[partX]
            
            maxlY = float('-inf') if partY == 0 else nums2[partY - 1]
            minrY = float('inf') if partY == y else nums2[partY]
            
            if maxlX <= minrY and maxlY <= minrX:
                if (x + y) % 2 == 0:
                    return (max(maxlX, maxlY) + min(minrX, minrY)) / 2.0
                else:
                    return float(max(maxlX, maxlY))
            elif maxlX > minrY:
                high = partX - 1
            else:
                low = partX + 1
                
        return 0.0
        
