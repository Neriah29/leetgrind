class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums[:]
        self.count = k
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.count]
        
        
