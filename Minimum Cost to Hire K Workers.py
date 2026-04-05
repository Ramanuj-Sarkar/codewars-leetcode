class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # the lowest wage / quality workers go to the front now
        ratio = sorted([(w / q, q) for w, q in zip(wage, quality)])
        max_heap = []
        quality_sum = 0
        max_ratio = 0.0
        
        for i in range(k):
            # it adds the wage / quality value, which shows what to multiply to get minimum wage
            max_ratio = max(max_ratio, ratio[i][0])
            # it adds the quality to the quality sum
            quality_sum += ratio[i][1]
            heapq.heappush(max_heap, -ratio[i][1])
        
        # hired the lowest wage / quality workers
        res = max_ratio * quality_sum
        
        for i in range(k, len(quality)):
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1] + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -ratio[i][1])
            # see if any higher wage / quality workers can work for lower total cost
            res = min(res, max_ratio * quality_sum)
        
        return res
