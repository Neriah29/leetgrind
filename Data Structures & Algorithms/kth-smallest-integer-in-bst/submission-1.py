# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodeCount = res = 0

        def dfs(node):
            nonlocal nodeCount, res
            if not node: return 

            dfs(node.left)
            nodeCount += 1
            if nodeCount == k:
                res = node.val
            dfs(node.right)

        dfs(root)
        return res


        