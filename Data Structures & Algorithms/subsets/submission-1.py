class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        strategy:
        at each step, you can either add it or not.
        so we only append when at the bottom of the decision tree.
        """
        res = []
        subset = []

        def backtrackDFS(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
    
            subset.append(nums[i])
            backtrackDFS(i+1)

            subset.pop()
            backtrackDFS(i+1)
            
        backtrackDFS(0)
        return res
