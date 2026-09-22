# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        I am thinking that this is kind of a dynamic programming problem
        at each node, the max path is max of the left and right

        base case:
        no node return 0
        1 node, return that nodes value

        recursive case:
        return the curval + max left and max right
        """
    
        res = 0

        def max_sum(node):
            nonlocal res
            if not node:
                return 0
            
            left_max = max_sum(node.left)
            right_max = max_sum(node.right)

            cur_sum = left_max + right_max + node.val
            cur_max_path_sum = max(left_max, right_max) + node.val
            res = max(res, cur_sum)
            return cur_max_path_sum

        max_sum(root)
        return res


            
