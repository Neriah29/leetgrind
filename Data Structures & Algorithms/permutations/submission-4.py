class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, arr):
            new_arr = []
            
            if i >= len(nums):
                return arr
            
            for n in range(len(arr)):
                for j in range(len(arr[n])+1):
                    cur_copy = arr[n].copy()
                    cur_copy.insert(j, nums[i])
                    new_arr.append(cur_copy)
            # print(new_arr)
            return dfs(i+1, new_arr)


 
        return dfs(0, [[]])
