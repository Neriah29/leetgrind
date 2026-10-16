from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dag = defaultdict(set)
        for course, req in prerequisites:
            dag[course].add(req)
        

        activity = [0] * numCourses
        def dfs(course):
            if activity[course] == 1:
                return False
            if activity[course] == 2:
                return True
            
            activity[course] = 1
            for req in dag[course]:
                if not dfs(req):
                    return False
            
            activity[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True 

