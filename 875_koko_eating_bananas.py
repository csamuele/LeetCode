class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        lowerBound, upperBound = 1, max(piles)
        minHoursToEat = 0
        while upperBound >= lowerBound:
            hoursToEat = 0
            mid = (upperBound + lowerBound) // 2
            for pile in piles:
                hoursPerPile = -(pile // -mid)
                hoursToEat += hoursPerPile
            if hoursToEat > h:
                lowerBound = mid + 1
            else:
                minHoursToEat = mid
                upperBound = mid - 1
        return minHoursToEat
solution = Solution()
solution.minEatingSpeed([30,11,23,4,20], 5)