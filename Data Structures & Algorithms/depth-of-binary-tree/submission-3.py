# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive case
        if not root:
            return 0       
        # l = 1 + (self.maxDepth(root.left))
        # r = 1 + (self.maxDepth(root.right))
        # return max(l, r)

        #iterative bfs:
        level = 0
        q = deque([root])
        while q:
            for node in range(len(q)):
                curr = q.popleft()
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
            level += 1
        return level

