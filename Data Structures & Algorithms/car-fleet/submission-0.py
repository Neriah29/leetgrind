class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = sorted([[p,s] for p, s in zip(position, speed)])[::-1]
        stack = []

        for p, s in pos:
            time = (target - p )/s
            stack.append(time)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)