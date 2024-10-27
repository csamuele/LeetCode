class Solution:
    def search1D(self, nums: list[int], target: int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lowerBound  = 1
        upperBound = len(nums) - 1

        while (lowerBound <= upperBound):
            midIndex = (upperBound + lowerBound) // 2
            if nums[midIndex] > target:
                upperBound = midIndex - 1
            elif nums[midIndex] < target:
                lowerBound = midIndex + 1
            else:
                return True
        return False
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        upperBound = len(matrix) - 1
        lowerBound = 0
        if target > matrix[-1][-1]:
            return False
        while (lowerBound <= upperBound):
            mid = (upperBound + lowerBound) // 2
            if target > matrix[mid][0]:
                if mid == upperBound or target < matrix[mid + 1][0]:
                    return self.search1D(matrix[mid], target)
                elif target > matrix[mid + 1][0]:
                    lowerBound = mid + 1
                else:
                    return True
            elif target < matrix[mid][0]:
                upperBound = mid - 1
            else:
                return True
        return False
solution = Solution()

solution.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15)
testMatrix = [[1,   2,  3,  4,  5], 
              [6,   7,  8,  9,  10], 
              [11,  12, 13, 14, 15], 
              [16,  17, 18, 19, 20], 
              [21,  22, 23, 24, 25]]
solution.searchMatrix([[1]], 0)
assert(solution.searchMatrix(testMatrix, 8))
assert(not solution.searchMatrix(testMatrix, 26))
assert(not solution.searchMatrix(testMatrix, -1))
assert(solution.searchMatrix(testMatrix, 16))
assert(solution.searchMatrix(testMatrix, 23))

