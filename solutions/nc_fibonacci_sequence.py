class Solution(object):
    def giveFibonacci(self, val:int):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if val <= 1:
            return val
        return self.giveFibonacci(val - 1) + self.giveFibonacci(val - 2)
    
solution = Solution()
print(solution.giveFibonacci(4))
print(solution.giveFibonacci(5))
print(solution.giveFibonacci(6))
        