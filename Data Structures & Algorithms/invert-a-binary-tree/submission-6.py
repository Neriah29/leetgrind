# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        recursive solution
        base case:
        None or no Children

        recursive case, swap both left and right children
        """

        if not root or not(root.left or root.right):
            return root
        
        def invert_tree(root):
            if not root:
                return 
            

            invert_tree(root.left)
            invert_tree(root.right)

            root.left, root.right = root.right, root.left

            return 
        invert_tree(root)
        return root