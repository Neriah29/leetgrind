class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxheap = [num for num in nums] 
        self.k = k
        heapq.heapify(self.maxheap)
        print(self.maxheap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.maxheap, val)
        result = heapq.nlargest(self.k, self.maxheap)
        return result[-1]

        
        
