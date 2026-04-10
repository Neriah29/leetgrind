class Solution:
    def search(self, nums: List[int], target: int) -> int:
        order = [[num, i] for i, num in enumerate(nums)]
        order.sort()
        l, r = 0, len(order)-1
        while l <= r:
            m = (l + r)//2
            if order[m][0] == target:
                return order[m][1]
            elif order[m][0] > target:
                r = m - 1
            elif order[m][0] < target:
                l = m + 1
        return -1