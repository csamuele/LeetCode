from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val: int = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        root = Node(node.val, node.neighbors)
        visited = {}
        queue = deque()
        visited[node.val] = root
        queue.append(root)
        while queue:
            currNode: Node = queue.popleft()
            newNeighbors: list[Node] = []
            for neighbor in currNode.neighbors:
                
                if neighbor.val not in visited:
                    newNeighbor = Node(neighbor.val, neighbor.neighbors)
                    newNeighbors.append(newNeighbor)
                    queue.append(newNeighbor)
                    visited[neighbor.val] = newNeighbor
                else:
                    newNeighbors.append(visited[neighbor.val])
            currNode.neighbors = newNeighbors
        return root
                
            
