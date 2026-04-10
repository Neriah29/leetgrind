class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        for num in nums:
            heapq.heappush(self.nums, -num)
        self.count = k
        

    def add(self, val: int) -> int:
        self.tmp = []
        heapq.heappush(self.nums, -val)
        for i in range(self.count):
            self.tmp.append(heapq.heappop(self.nums))
        res = self.tmp[-1]
        for i in range(len(self.tmp)):
            heapq.heappush(self.nums, self.tmp[i])
        return -res
        
        
