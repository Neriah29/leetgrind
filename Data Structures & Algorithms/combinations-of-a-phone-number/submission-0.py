class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToText = {
                    2 : ["a", "b", "c"], 3 : ["d", "e", "f"],
                    4 : ["g", "h", "i"], 5: ["j", "k", "l"],
                    6 : ["m", "n", "o"], 7: ["p", "q", "r", "s"],
                    8 : ["t", "u", "v"], 9: ["w", "x", "y", "z"]
                    }
        
        """
        plan:
        have a similar dfs to that of parentheses 
        structure:
        keep going down the tree until num > len(digits)
        then you append to 
        the res
        """

        res = []

        def dfs(h, cur):
            if h >= len(digits):
                res.append(cur)
                return
            k = digits[h]
            for j in range(len(numToText[int(k)])):
                dfs(h+1, cur + numToText[int(k)][j])
                
        dfs(0, "" ) 
        return res if digits else []
        



        

