from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = list(map(lambda stone: -stone, stones))
        heapify(stones)

        while len(stones) > 1:
            stone1: int = heappop(stones)
            stone2: int = heappop(stones)
            smashResult = -abs(stone1 - stone2)
            if smashResult < 0:
                heappush(stones, smashResult)
        
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]
        
solution = Solution()
solution.lastStoneWeight([2,3,6,2,4]) == 1