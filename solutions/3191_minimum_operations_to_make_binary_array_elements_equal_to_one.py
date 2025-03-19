class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                count += 1

        if not(nums[-1]) or not(nums[-2]):
            return -1
        return count
    
sol = Solution();
sol.minOperations([0,1,1,1,0,0])