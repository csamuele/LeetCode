class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []
        def helper(i):
            if i >= len(nums):
                res.append(subset.copy[:])
                return
            
            subset.append(nums[i])
            helper(i + 1)

            subset.pop()
            helper(i + 1)
        helper(0)
        return res

solution = Solution()
print(solution.subsets([1, 2, 3, 4]))