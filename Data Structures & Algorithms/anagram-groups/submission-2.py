class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        res = []
        for i in range(len(strs)):
            s = tuple(sorted(strs[i]))
            if s in check:
                res[check[s]].append(strs[i])
            else:
                check[s] = len(res)
                res.append([strs[i]])
        
        return res