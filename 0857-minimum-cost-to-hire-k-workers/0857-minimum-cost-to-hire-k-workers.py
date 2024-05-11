import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = []

        for i in range(n):
            workers.append((wage[i] / quality[i], quality[i]))
        
        workers.sort()

        max_heap = []
        total_quality = 0
        min_cost = float('inf')
        sum_quality = 0

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q
            sum_quality += q

            if len(max_heap) > k:
                sum_quality += heapq.heappop(max_heap)

            if len(max_heap) == k:
                min_cost = min(min_cost, sum_quality * ratio)

        return min_cost