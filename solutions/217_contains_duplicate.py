class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
                if map[num] > 1:
                    return True
            else:
                map[num] = 1
        return False
    
solution = Solution()
solution.containsDuplicate([1,2,3,1])