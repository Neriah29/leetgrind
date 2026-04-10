class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l, r = 0, 0
        t = []
        while r < len(temperatures) :
            if temperatures[r] > temperatures[l]:
                t.append(r - l)
                l += 1
                r = l + 1
            else:
                if r < len(temperatures) - 1:
                    r += 1 
                else:
                    t.append(0)
                    l += 1
                    r = l + 1
        t.append(0)
        return t
            
            
        
        