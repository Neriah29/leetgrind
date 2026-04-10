class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum_dict = {}
        for num in numbers:
            sum_dict[num] = target - num
        for num in numbers:
            if sum_dict[num] in numbers and sum_dict[num] != num:
                idx1 = numbers.index(num) + 1
                idx2 = numbers.index(sum_dict[num]) + 1
                if idx1 > idx2:
                    return [idx2, idx1]
                else:
                    return [idx1, idx2]
