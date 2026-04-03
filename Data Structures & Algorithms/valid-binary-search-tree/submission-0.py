# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        the stratgy is, we are going to run a dfs but using bounds 
        """

        def dfs(root, lower_bound, upper_bound):
            if not root:
                return True
            
            if root.val > lower_bound and root.val < upper_bound:
                return (True and dfs(root.left, lower_bound, root.val) and 
                        dfs(root.right, root.val, upper_bound))
            
            return False
            
        return dfs(root, float("-inf"), float("inf"))