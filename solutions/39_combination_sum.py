class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def helper(i: int, subset: list[int], total: int):
            if total > target or i >= len(nums):
                return
            if total == target:
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            helper(i, subset, total + nums[i])

            subset.pop()
            helper(i + 1, subset, total)
        helper(0, [], 0)
        return res
