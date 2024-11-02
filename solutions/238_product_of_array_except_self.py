class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = nums[i] * prefix
        suffix = 1
        for i in reversed(range(len(nums))):
            res[i] = res[i] * suffix
            suffix = suffix * nums[i]
        return res