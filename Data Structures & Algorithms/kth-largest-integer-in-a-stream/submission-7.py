class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        we are trying to keep the heap at a max of k elements
        """
        self.k = k
        self.heap = [num for num in nums]
        heapq.heapify(self.heap)
        print(f"Before --> {self.heap}")
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        print(f" After --> {self.heap}")


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # print(self.heap)
        return self.heap[0]
        
