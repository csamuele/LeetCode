#negative marking
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            nums[abs(nums[i]) - 1] *= -1



#linked list
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
s = Solution()
s.findDuplicate([1, 3, 4, 2, 2])