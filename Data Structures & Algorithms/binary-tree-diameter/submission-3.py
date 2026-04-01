# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Approach:
        create a helper function 
        if not node return 0 
        it is basically height of left height or right at each node 
        so at each node we check the diameter from the height of the left 
        to the 
        """
        max_diam = 0
        def diameter(root):
            nonlocal max_diam
            if not root:
                return 0
            
            #we check if the max is at this point, & we take the max
            l, r = diameter(root.left), diameter(root.right)
            max_diam = max(l + r, max_diam)
            return max(l, r) + 1
        
        diameter(root)
        return max_diam

