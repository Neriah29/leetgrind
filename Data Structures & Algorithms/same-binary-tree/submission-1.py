# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1, l2 = [], []
        def dfs(head, array):
            if not head:
                array.append(None)
                return 
            array.append(head.val)
            dfs(head.left, array)
            dfs(head.right, array)
        
        dfs(p, l1)
        dfs(q, l2)
        print(l1, l2)
        return l1 == l2
        


        