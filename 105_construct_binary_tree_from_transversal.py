# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(preorder) < 1:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        preorderLeft = preorder[1 : mid + 1]
        inorderLeft = inorder[0 : len(preorderLeft)]
        preorderRight = preorder[mid + 1:]
        inorderRight = inorder[len(preorderLeft) + 1 :]
        return TreeNode(preorder[0], self.buildTree(preorderLeft, inorderLeft), self.buildTree(preorderRight, inorderRight))
        
            
inorder = [2, 3, 4, 5, 6, 7, 8]
preorder = [5, 3, 2, 4, 7, 6, 8]
solution = Solution()
solution.buildTree(preorder, inorder)
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution.buildTree(preorder, inorder)
solution.buildTree([], [])
test= 0
        