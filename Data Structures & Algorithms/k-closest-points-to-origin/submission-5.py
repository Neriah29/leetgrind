class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        create a distances array corresponding to the distances of each point at the same index
        """

        res = []
        distances = []
        
        for i in range(len(points)):
            d = (points[i][0]**2 + points[i][1]**2)**0.5
            distances.append([d,i])
        
        heapq.heapify(distances)

        for i in range(k):
            res.append(points[heapq.heappop(distances)[1]])
        
        return res
