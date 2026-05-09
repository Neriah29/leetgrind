class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-num for num in nums]
        heapq.heapify(self.heap)
        self.k = k


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        print(self.heap)
        tmp = []
        for i in range(self.k-1):
            tmp.append(heapq.heappop(self.heap))
        curr = self.heap[0]
        for i in range(len(tmp)):
            heapq.heappush(self.heap, tmp.pop())
        return -curr

        
