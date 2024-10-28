# Definition for a binary tree node.

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)

        levels: list[list[int]] = []
        while len(queue) > 0:
            level: list[int] = []
            for i in range(len(queue)):
                curr: TreeNode = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            levels.append(level)
        res: list[int] = []
        for level in levels:
            res.append(level[-1])
        return res