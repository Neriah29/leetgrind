class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        flag = False
        a = sorted(list(s1))

    
        for i in range(len(s2) - len(s1)+1):
            if s2[i] in s1:
                b = sorted(s2[i: i +len(s1)])
                if b == a:
                    return True
        
        return False
                