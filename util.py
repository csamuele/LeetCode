from typing import Optional
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def buildBinaryTreeFromList(arr:list[Optional[int]]):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = deque()
    queue.append(root)
    i = 1
    while i < len(arr):
        curr: TreeNode = queue.popleft()
        if arr[i] is not None:
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
        i += 1
        if i < len(arr) and arr[i] is not None: 
            curr.right = TreeNode(arr[i])
            queue.append(curr.right)
        i += 1  
    return root

