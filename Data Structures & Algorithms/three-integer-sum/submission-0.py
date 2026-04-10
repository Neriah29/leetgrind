class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        def isnotduplicate(sublist, biggerlist):
            subsort = sorted(sublist)
            for sequence in biggerlist:
                if sorted(sequence) == subsort:
                    return False
            return True

        for idx in range(len(nums)-2):
            for idx2 in range(idx+1, len(nums)-1):
                temp = nums[idx] + nums[idx2]
                third = -temp
                if third in nums[idx2+1:]:
                    triplet = [nums[idx], nums[idx2], third]
                    if isnotduplicate(triplet, result):
                        result.append(triplet)

        return result


