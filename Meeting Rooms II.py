class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # return zero if it's empty
        if not intervals:
            return 0

        intervals.sort()
        minHeap = []

        for start,end in intervals:
            # you can't add the meeting if it starts before the end of the previous one
            if minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)
            
            # add the end of the meeting being added
            heapq.heappush(minHeap,end)

        return len(minHeap)
  
