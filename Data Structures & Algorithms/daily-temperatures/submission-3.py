class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        initialize an empty array of 0s
        """

        res = [0 for _ in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()

            stack.append((i, temperatures[i]))

        return res   
