# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        response = []
        def helper(root):
            if not root:
                return []
            helper(root.left)
            response.append(root.val)
            helper(root.right)
        helper(root)
        return response
    def preorderTransversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        response = []
        def helper(root):
            if not root:
                return
            response.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return response
    
    
solution = Solution()
testCase = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8)))
print(solution.inorderTraversal(testCase))
print(solution.preorderTransversal(testCase))
