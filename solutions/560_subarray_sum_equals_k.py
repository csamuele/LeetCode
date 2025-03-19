class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sumCount = {}
        currSum = 0
        res = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum == k:
                res += 1
            if currSum - k in sumCount:
                res += sumCount[currSum - k]
            sumCount[currSum] = sumCount.get(currSum, 0) + 1
        return res
