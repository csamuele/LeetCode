class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currentSum = 0
        maxSum = nums[0]
        for num in nums:
            currentSum += num
            maxSum = max(currentSum, maxSum)
            if currentSum < 0:
                currentSum = 0
        return maxSum