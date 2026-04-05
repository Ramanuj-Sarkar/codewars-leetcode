class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # you get the first k elements into a minheap
        # now heap[0] is the minimum of these k
        heap = nums[:k]
        heapq.heapify(heap)
        
        # you get the values that are bigger in the rest
        # the idea is to take away every value smaller
        # than the kth largest element
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]
        
