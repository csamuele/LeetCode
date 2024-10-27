# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right
class Solution(object):
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        queue = deque()

        if root:
            queue.append(root)
        
        res: List[List[int]] = []
        while(len(queue) > 0):
            subArray: list[int] = []
            for i in range(len(queue)):
                curr: TreeNode = queue.popleft()
                subArray.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(subArray)
        return res