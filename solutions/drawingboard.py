import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        numRows = len(moveTime)
        numCols = len(moveTime[0])
        
        # Priority queue to store (current_time, x, y)
        minHeap = [(0, 0, 0)]  # Start at (0, 0) with time 0
        arrivalTime = [[float('inf')] * numCols for _ in range(numRows)]
        arrivalTime[0][0] = 0
        
        # Directions for adjacent rooms (down, up, right, left)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            currentTime, row, col = heapq.heappop(minHeap)

            # If we reached the target room (numRows - 1, numCols - 1)
            if (row, col) == (numRows - 1, numCols - 1):
                return currentTime

            # Explore adjacent rooms
            for dRow, dCol in directions:
                newRow, newCol = row + dRow, col + dCol

                if 0 <= newRow < numRows and 0 <= newCol < numCols:
                    waitTime = max(moveTime[newRow][newCol] - currentTime, 0)
                    newArrivalTime = currentTime + 1 + waitTime

                    # Only push to the queue if we found a better arrival time
                    if newArrivalTime < arrivalTime[newRow][newCol]:
                        arrivalTime[newRow][newCol] = newArrivalTime
                        heapq.heappush(minHeap, (newArrivalTime, newRow, newCol))

        return -1  # Return -1 if the target room is unreachable

solution = Solution()
answer = solution.minTimeToReach([
    [94,79,62,27,69,84],
    [6,32,11,82,42,30]
])   
answer = solution.minTimeToReach([
    [0, 4],
    [4, 4]
])   
print(answer)    
       