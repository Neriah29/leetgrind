class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToAlph = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        res = []

        def dfs(numIndex, curString):
            if numIndex >= len(digits):
                res.append(curString)
                return
            for alphIndex in range(len(numToAlph[digits[numIndex]])):
                dfs(numIndex + 1, curString + numToAlph[digits[numIndex]][alphIndex])
        dfs(0, "")

        return res if len(digits) else []
            

