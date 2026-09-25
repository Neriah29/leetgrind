class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        I feel this is a straight forward heap question 

        for each point, we get the get the distance and then append it 
        to a datastructure that will be heapified
        """

        def distance(x,y):
            pass
        

        min_distance_heap = [(distance(x,y),[x,y]) for x,y in points]
        heapq.heapify(min_distance_heap)

        res = heapq.nsmallest(k, min_distance_heap)

        res = [res[i][1] for i in range(len(res)) ]

        return res

        
