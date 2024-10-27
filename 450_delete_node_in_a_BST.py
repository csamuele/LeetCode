# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minValue(self, root):
        if root and root.left:
            return self.minValue(root.left)
        else:
            return root.val
    def deleteNode(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        
        if not root:
            return None
        
        if val > root.val:
            root.right = self.deleteNode(root.right, val)
        elif val < root.val:
            root.left = self.deleteNode(root.left, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minVal = self.minValue(root.right)
                root.val = minVal
                root.right = self.deleteNode(root.right, minVal)
        return root
solution = Solution()

testCase = TreeNode(5, TreeNode(3, right=TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8)))
solution.deleteNode(testCase, 5)