# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        I am thinking of a recursive solution for this
        base case:
        return true if not node, or not nodes children
        """
        flag = True

        def height(node):
            nonlocal flag
            if not node:
                return 0 
            
            lheight = height(node.left)
            rheight = height(node.right)

            if abs(lheight - rheight) > 1:
                flag = False

            return 1 + max(lheight, rheight)
        
        height(root)
        return flag
