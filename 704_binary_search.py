class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lowIndex  = 0
        highIndex = len(nums) - 1

        while (lowIndex <= highIndex):
            midIndex = (highIndex + lowIndex) // 2
            if nums[midIndex] > target:
                highIndex = midIndex - 1
            elif nums[midIndex] < target:
                lowIndex = midIndex + 1
            else:
                return midIndex
        return -1
    
test = Solution()
test.search([-1,2,3,5,9,12], 2)