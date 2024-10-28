from heapq import heapify, heappop, heappush

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minHeap = []
        for x, y in points:
            distFromOrigin = (x ** 2 + y ** 2)
            minHeap.append((distFromOrigin, x, y))
        heapify(minHeap)
        res: list[int] = []
        for i in range(k):
            point = heappop(minHeap)
            d, x, y = point
            res.append([x, y])
        return res
solution = Solution()

solution.kClosest([[0,2],[2,2]], 1)
