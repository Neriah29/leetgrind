class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(set(nums))
        max_count = 0
        counter = 1
        flag = False
        if len(sort) > 1:
            for idx in range(len(sort)-1):
                if sort[idx +1] == sort[idx] + 1:
                    flag = True
                else:
                    flag = False
                if flag:
                    counter += 1
                else:
                    counter = 1
                if counter > max_count:
                    max_count = counter   
        elif len(sort) == 1:
            max_count = 1
        else:
            max_count = 0
        return max_count   

            
        