# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        the solution i am thinking of is not very efficient. 
        seems to be quadratic in worst case
        base cases:
        """
        if not subRoot: #empty is always going to be subset
            return True
        if not root:
            return False #if subset not empty but bigger node is

        if self.isSameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    def isSameTree(self, root, subroot):

        if not root and not subroot:
            return True 
        if not root or not subroot:
            return False
        if root.val == subroot.val:
            return self.isSameTree(root.left, subroot.left) and self.isSameTree(root.right, subroot.right)
        else:
            return False