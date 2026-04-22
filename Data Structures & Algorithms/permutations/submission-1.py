class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        run the dfs down to leaf
        base case - [[]]
        next, iterate over each permutation
        within each permutation, iterate over that and make copies of each possible position
        of the next i 
        keep cycling up
        """

        if not nums:
            return [[]]
        res = []
        permutations = self.permute(nums[1:])
        for permutation in permutations:
            for i in range(len(permutation)+1):
                curPer = permutation.copy()
                curPer.insert(i, nums[0])
                res.append(curPer)
        
        return res