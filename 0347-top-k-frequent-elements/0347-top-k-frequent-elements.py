from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap =[]
        for num, freq in c.items():
            if len(heap) < k:
                heappush(heap, (freq,num))
            elif heap[0][0] < freq:
                heappushpop(heap, (freq,num))
        
        return [num for _, num in heap]