# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        by default, we can set the return to be True (maybe a flag)
        we check the height for both left and right. return them == 
        """
        flag = True
        def height(root):
            nonlocal flag
            """
            here, we want to check the height for left and right and
            change self.flag if wrong
            """
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            if abs(l - r) > 1:
                flag = False
            return 1 + max(l, r)
        height(root)
        return flag