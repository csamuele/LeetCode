class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        lowerBound = 0
        currSum = 0
        res = len(nums) + 1
        for upperBound in range(len(nums)):
            currSum += nums[upperBound]
            while currSum >= target:
                res = min(upperBound - lowerBound + 1, res)
                currSum -= nums[lowerBound]
                lowerBound += 1
            
        return res if res != len(nums) + 1 else 0