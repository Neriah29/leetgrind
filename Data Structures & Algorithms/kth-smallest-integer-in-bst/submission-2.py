# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count, res = 0, None

        def dfs(node):
            nonlocal count, res
            if not node:
                return
            
            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
                return 
    
            dfs(node.right)
        dfs(root)
        return res
