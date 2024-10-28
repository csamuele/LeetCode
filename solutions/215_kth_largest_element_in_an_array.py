

from heapq import heapify, heappop


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        res = 0
        for i in range(k):
            res = heappop(nums)

        return -res