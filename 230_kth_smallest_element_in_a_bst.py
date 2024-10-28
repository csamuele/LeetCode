# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def inorder(self, root, count, ans, k):
        if not root:
            return
        self.inorder(root.left, count, ans, k)
        if ans[0]:
            return
        count[0] += 1
        if count[0] == k:
            ans[0] = root.val
            return
        self.inorder(root.right, count, ans, k)
    

    def kthSmallest(self, root, k):
        #putting them in arrays is a hack to make them pass by reference
        count = [0]
        ans = [None]
        self.inorder(root, count, ans, k)
        return ans
        
    
        
solution = Solution()
testCase1 = TreeNode(2, TreeNode(1), TreeNode(3))
testCase2 = TreeNode(4, TreeNode(3, TreeNode(2)), TreeNode(5))
solution.kthSmallest(testCase1, 1)