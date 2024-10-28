from util import buildBinaryTreeFromList
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def helper(node, currSum):
            if not node:
                return False
            currSum += node.val
            
            if not node.left and not node.right:
                if currSum == targetSum:
                    return True
                else:
                    return False
            if helper(node.left, currSum):
                return True
            if helper(node.right, currSum):
                return True
            return False
        return helper(root, 0)

testCase = buildBinaryTreeFromList([5,4,8,11,None,13,4,7,2,None,None,None,1])
solution = Solution()
solution.hasPathSum(testCase, 22)