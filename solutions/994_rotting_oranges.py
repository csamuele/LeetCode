from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        freshOranges = 0
        queue = deque()
        hours = 0
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    freshOranges += 1
                    continue
                if grid[row][column] == 2:
                    queue.append((row, column))
                    continue
        while queue:
            if not freshOranges:
                return hours
            for i in range(len(queue)):
                row, col = queue.popleft()
                for direction in directions:
                    rowMod, colMod = direction
                    newRow, newCol = row + rowMod, col + colMod
                    if (0 <= newRow < rows and 
                        0 <= newCol < columns and
                        grid[newRow][newCol] == 1
                    ):
                        freshOranges -= 1
                        
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
         
            hours += 1
        if not freshOranges:
            return hours
        else:
            return -1


grid=[
    [1,1,0],
    [0,1,1],
    [0,1,2]]
grid=[
    [2,1,1],
    [1,1,0],
    [0,1,1]]
solution = Solution()
print(solution.orangesRotting(grid))