# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True

        def height(root):
            nonlocal balance
            if not root:
                return 0 

            leftHeight, rightHeight = height(root.left), height(root.right) 
            currHeight = max(leftHeight, rightHeight) +1
            if abs(leftHeight - rightHeight) > 1:
                balance = False
            
            return currHeight

        height(root)
        return balance