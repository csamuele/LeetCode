from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        count = 0
        visited = set()
        def bfs(row, column):
            queue = deque()
            visited.add((row, column))
            queue.append(((row, column)))

            while queue:
                row, column = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for direction in directions:
                    rowMod, columnMod = direction
                    newRow, newColumn = row + rowMod, column + columnMod
                    if (
                        newRow in range(rows) and
                        newColumn in range(columns) and
                        grid[newRow][newColumn] == '1' and
                        (newRow, newColumn) not in visited
                        ):
                        queue.append((newRow, newColumn))
                        visited.add((newRow, newColumn))


            
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1' and (row, column) not in visited:
                    count += 1
                    bfs(row, column)
        return count
    
grid = [["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]

solution = Solution()
solution.numIslands(grid)