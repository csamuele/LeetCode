class Solution:
    def trap(self, height: list[int]) -> int:
        maxLeft = maxRight = 0
        totalWater = 0
        leftPtr, rightPtr = 0, len(height) - 1
        while leftPtr <= rightPtr:
            leftHeight, rightHeight = height[leftPtr], height[rightPtr]
            if leftHeight <= rightHeight:
                waterHere = max(maxLeft - leftHeight, 0)
                totalWater += waterHere
                maxLeft = max(leftHeight, maxLeft)
                leftPtr += 1
            if rightHeight < leftHeight:
                waterHere = max(maxRight - rightHeight, 0)
                totalWater += waterHere
                maxRight = max(rightHeight, maxRight)
                rightPtr -= 1
        return totalWater
            