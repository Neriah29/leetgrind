# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def dfs(root):
            nonlocal depth

            if not root:
                return 0
            
            leftHeight, rightHeight = dfs(root.left), dfs(root.right)

            return max(leftHeight, rightHeight) + 1
        
        return dfs(root)


        
