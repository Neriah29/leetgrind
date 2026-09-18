# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        for sure a bfs implementation 
        """

        #initialize queue with root 
        if not root: return []
        queue = deque([root])
        res = []
        
        while queue:
            cur_row = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_row.append(node.val)
            res.append(cur_row)
        
        return res 
                