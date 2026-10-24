class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        g = defaultdict(set)
        for course, prereq in prerequisites:
            g[course].add(prereq)

        status = [0] * numCourses

        def dfs(course):
            if status[course] == 1:
                return False

            if status[course] ==  2:
                return True

            status[course] = 1

            for prereq in g[course]:
                if dfs(prereq) == False:
                    return False
            
            status[course] = 2
            res.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return res 
