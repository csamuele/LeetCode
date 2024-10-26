class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left_pointer = 0
        for right_pointer in range(len(nums)):
            if (nums[right_pointer] != val):
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1
        return left_pointer

        
