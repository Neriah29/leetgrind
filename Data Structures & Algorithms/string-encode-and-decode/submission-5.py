class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for element in strs:
            s += element + ";"
        return s

    def decode(self, s: str) -> List[str]:
        lst = s.split(";")[:-1]
        if s == " ":
            return [""]
        elif s == [""]:
            return []
        else:
            return lst
