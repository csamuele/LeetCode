class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        #edge cases
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        rows, columns = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid.append([0] * columns)

        for row in range(rows -1, -1, -1):
            obstacleGrid[row].append(0)
            for column in range(columns - 1, -1, -1):
                if obstacleGrid[row][column] == 1:
                    obstacleGrid[row][column] = 0
                elif row == rows - 1 and column == columns - 1:
                    obstacleGrid[row][column] = 1
                else:
                    obstacleGrid[row][column] = obstacleGrid[row][column + 1] + obstacleGrid[row + 1][column]
        return obstacleGrid[0][0]