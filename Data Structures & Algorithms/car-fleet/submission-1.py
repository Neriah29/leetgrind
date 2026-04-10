class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#approach 
#have a stack
#sort the positions in reverse order
#starting with the closest to target, check t(ime) that car
#will reach target.
#stack will be full of times

        stack = []
        position = [(p, s) for p,s in zip(position, speed)]
        position.sort(reverse = True)
        for p, s in position:
            t = (target - p)/s
            if stack and t <= stack[-1]:
                continue
            else:
                stack.append(t)
        
        return len(stack)