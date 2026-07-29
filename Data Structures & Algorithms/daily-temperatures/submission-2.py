class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#approach using a stack 
# iterate through, checking in the stack if the curr is > than
#last index in the stack.
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            #check if curr is greater than the elements in the stack
            #currently
            while stack and t > stack[-1][1]:
                curr = stack.pop()
                res[curr[0]] = i - curr[0]
            stack.append((i,t))
        return res

            