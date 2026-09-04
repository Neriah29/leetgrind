# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        this is a bfs problem
        """

        if not root:
            return []

        q =  deque([root])
        res = []
        while q:
            qLength = len(q)
            for i in range(qLength):
                currNode = q.popleft()
                if currNode.left: q.append(currNode.left)
                if currNode.right: q.append(currNode.right)
                if i + 1 == qLength: res.append(currNode.val)
        return res 
            