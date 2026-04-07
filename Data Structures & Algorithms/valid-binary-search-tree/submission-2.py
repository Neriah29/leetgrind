# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag = True 
        def dfs(node, low, high):
            nonlocal flag
            if node: 
                if node.val >= high or node.val <=low:
                    flag = False
                dfs(node.left, low, node.val)
                dfs(node.right, node.val, high)

        dfs(root, float("-inf"), float("inf"))
        return flag