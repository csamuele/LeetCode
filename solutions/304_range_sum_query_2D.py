class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.prefixSums = [[0] * len(matrix[0]) for row in matrix]
        for row in range(len(matrix)):
            rowSum = 0
            for col in range(len(matrix[0])):
                currVal = matrix[row][col]
                rowSum += currVal
                if row < 1:
                    self.prefixSums[row][col] = rowSum
                else:
                    self.prefixSums[row][col] = rowSum + self.prefixSums[row - 1][col]
            



        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topRectSum = self.prefixSums[row1 - 1][col2] if row1 > 0 else 0
        leftRectSum = self.prefixSums[row2][col1 - 1] if col1 > 0 else 0
        intersectRectSum = self.prefixSums[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.prefixSums[row2][col2] - topRectSum - leftRectSum + intersectRectSum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
numMatrix = NumMatrix([
    [3,0,1,4,2],
    [5,6,3,2,1],
    [1,2,0,1,5],
    [4,1,0,1,7],
    [1,0,3,0,5]])

numMatrix.sumRegion(2, 1, 4, 3)