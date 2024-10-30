class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, columns = m - 1, n - 1 
        prevRow = [1] * n
        for row in range(rows - 1, -1, -1):
            currRow = [1] * n
            for column in range(columns - 1, -1, -1):
                currRow[column] = currRow[column + 1] + prevRow[column]
            prevRow = currRow
        return prevRow[0]