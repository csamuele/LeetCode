class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        valueCounter = [0, 0, 0]

        for num in nums:
            valueCounter[num] += 1

        index = 0
        for value in range(len(valueCounter)):
            for numOfEachValue in range(valueCounter[value]):
                nums[index] = value
                index += 1
        
        return nums