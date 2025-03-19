class Solution:
    # def removeDuplicates(self, nums: list[int]) -> int:
    #     rightPtr = len(nums) - 1
    #     leftPtr = rightPtr - 2
    #     while leftPtr >= 0:
    #         if nums[leftPtr] == nums[rightPtr]:
    #             nums.pop(rightPtr)
    #         rightPtr -= 1
    #         leftPtr -= 1

    #More efficient
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        leftPtr = 2
        for rightPtr in range(2, len(nums)):
            if nums[leftPtr - 2] != nums[rightPtr]:
                nums[leftPtr] = nums[rightPtr]
                leftPtr += 1
        return leftPtr