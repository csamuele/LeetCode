class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        globalMax = globalMin = nums[0]
        currentMax = currentMin = total = 0
        for num in nums:
            total += num
            currentMax = max(currentMax + num, num)
            currentMin = min(currentMin + num, num)
            globalMax = max(currentMax, globalMax)
            globalMin = min(currentMin, globalMin)
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax

