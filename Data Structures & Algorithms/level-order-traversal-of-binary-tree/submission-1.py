# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        this appears to be a bfs problem 
        we have parent res list which contains the other lists
        per iteration nested list goes to empty list
        """
        if not root:
            return []
        
        #now, we are sure we would not encounter issues initializing our deque withn root
        q = deque([root])
        res = []
        while q:
            nest = []
            num = len(q)
            for i in range(num):
                currNode = q.popleft()
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
                nest.append(currNode.val)
            res.append(nest)
        return res


            


