# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        #we are going to run a bfs and 
        #at every level, we add the last pop, to the res list we eventually return 

        q = deque([root])
        res = []
        while q:
            q_length = len(q)
            for idx in range(q_length):
                currNode = q.popleft()
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
                
                if idx == q_length - 1: res.append(currNode.val)
            
        return res