class Solution:
    def maxArea(self, height: list[int]) -> int:
        largest = 0 
        lowerBnd, upperBnd = 0, len(height) - 1
        while lowerBnd < upperBnd:
            leftWall, rightWall = height[lowerBnd], height[upperBnd]
            lowWall = min(leftWall, rightWall)
            volume = lowWall * (upperBnd - lowerBnd)
            largest = max(volume, largest)
            if leftWall <= rightWall:
                lowerBnd += 1
            if rightWall <= leftWall:
                upperBnd -= 1
        return largest

solution = Solution()
solution.maxArea([1,8,6,2,5,4,8,3,7])