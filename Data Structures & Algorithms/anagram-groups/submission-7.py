class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        solution i am thinking of seems to be O(n * w)
        where n = len(strs) and w = max length of a word

        iterate over strs and make a counter dict, possibly convert that to a tuple?
        the tuple will point to the index of the list in the res
        """
        res = []
        checkMap = {}

        for idx in range(len(strs)):
            #for each we get the tuple containing the frequencies
            curCountTuple = frozenset(Counter(strs[idx]).items())

            #check if the tuple is alr in the map
            #if it is already in, then go to the index of res and append
            if checkMap and curCountTuple in checkMap:
                resIndex = checkMap[curCountTuple]
                res[resIndex].append(strs[idx])
            else:
                res.append([strs[idx]])
                checkMap[curCountTuple] = len(res) - 1
            
        return res


