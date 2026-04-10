class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
#Approach
#going to have two pointers going over s2
#l will be len s1 away from r
#
        if len(s1) > len(s2):
            return False

        f1 = defaultdict(int)
        f2 = defaultdict(int)

        for i in range(len(s1)):
            f1[s1[i]] += 1
        l = 0
        for r in range(len(s2)):
            f2[s2[r]] += 1
            if r - l +1 != len(s1):
                continue
            else:
                if f1 == f2:
                    return True 
                else:
                    f2[s2[l]] -= 1
                    if not f2[s2[l]]: f2.pop(s2[l])
                    l += 1
        
        return False



