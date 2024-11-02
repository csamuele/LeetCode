class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        uniqueVals = set()
        for num in nums:
            if num not in uniqueVals:
                uniqueVals.add(num)
        res = 0
        for num in uniqueVals:
            if num - 1 not in uniqueVals:
                length = 1
                while(num + length) in uniqueVals:
                    length += 1
                res = max(res, length)
        return res