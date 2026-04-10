class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        if len(strs):
            for i in range(len(strs)):
                if i:
                    s += "(space)" + strs[i]
                else:
                    s += strs[i]
            return s
        else:
            return "empty"

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        return s.split("(space)")


