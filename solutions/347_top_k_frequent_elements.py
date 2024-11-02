from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        heap = []
        for key in count.keys():
            heappush(heap, (count[key], key))
            if len(heap) > k:
                heappop(heap)
        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])
        return res