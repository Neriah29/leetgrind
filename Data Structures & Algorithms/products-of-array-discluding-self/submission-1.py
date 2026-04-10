import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output =[]
        for num_idx in range(len(nums)):
            if num_idx == 0:
                output.append(math.prod(nums[1:]))
            elif num_idx == len(nums)-1:
                output.append(math.prod(nums[:-1]))
            else:
                value1 = math.prod(nums[:num_idx])
                value2 = math.prod(nums[num_idx+1:])
                output.append(value1 * value2)
        return output