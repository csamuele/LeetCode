from heapq import heappush, heappop
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return
        rows, columns = len(grid), len(grid[0])
        visited = set()
        islandHeap = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(row: int, column: int) -> int:
            queue = deque()
            queue.append((row, column))
            count = 1
            while queue:
                row, column = queue.popleft()
                for direction in directions:
                    rowMod, columnMod = direction
                    newRow, newColumn = row + rowMod, column + columnMod
                    if (
                        newRow in range(rows) and
                        newColumn in range(columns) and
                        grid[newRow][newColumn] == 1 and
                        (newRow, newColumn) not in visited
                    ):
                        queue.append((newRow, newColumn))
                        visited.add((newRow, newColumn))
                        count += 1
            return count
        area = 0

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1 and (row, column) not in visited:
                    visited.add((row, column))
                    area = max(area, bfs(row, column))

        return area
    
grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

solution = Solution()
solution.maxAreaOfIsland(grid)