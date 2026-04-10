class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        plan:
        so i am thinking of re initializing a diff list to contain the idx and 
        euclidean distance from the origin
        **create a function to calculate the origin
        make a new list
        """

        def distance(x, y):
            dist = (x**2 + y**2)**0.5
            print (x,y,res)
            return dist

        res = []
        distanceArray = []
        for i in range(len(points)):
            element = (distance(points[i][0], points[i][1]), i)
            heapq.heappush(distanceArray, element)

        for i in range(k):
            curr = heapq.heappop(distanceArray)
            res.append(points[curr[1]])

        return res