class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefix = nums[:]
        postfix = nums[:]
        length = len(nums)
        for i in range(length):
            if i > 0:
                prefix[i] += prefix[i - 1]
        for i in reversed(range(length)):
            if i < length - 1:
                postfix[i] += postfix[i + 1]
        for i in range(length):
            if postfix[i] == prefix[i]:
                return i
        return -1


