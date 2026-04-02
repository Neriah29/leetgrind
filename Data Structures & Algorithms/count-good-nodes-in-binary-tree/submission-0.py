# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        this has to be a dfs since we are using paths 
        the function takes in the min at that point 
        """

        count = 0
        def dfs(root, currMax):
            nonlocal count
            if not root:
                return 
            if root.val >= currMax:
                count += 1
                currMax = root.val

            dfs(root.left, currMax)
            dfs(root.right, currMax)

        dfs(root, -float("inf"))
        return count
            