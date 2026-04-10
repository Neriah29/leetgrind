# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        array1, array2 = [], []
        def dfs(node, array):
            if not node:
                array.append(None)
                return
            
            array.append(node.val)
            dfs(node.left, array)
            dfs(node.right, array)
            
        dfs(p, array1)
        dfs(q, array2)
        return array1 == array2
