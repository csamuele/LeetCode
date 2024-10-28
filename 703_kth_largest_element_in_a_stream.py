from heapq import heapify, heappop, heappush


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.minHeap = nums
        heapify(self.minHeap)
        self.k = k
        while len(self.minHeap) > k:
            heappop(self.minHeap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)