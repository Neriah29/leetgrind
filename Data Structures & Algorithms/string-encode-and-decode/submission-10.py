class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        here, we are trying to change the list of strings to a string
        we can use join
        """
        if strs:
            res = "*space*".join(strs)
            return res
        else:
            return "*empty*"


    def decode(self, s: str) -> List[str]:
        if s == "*empty*":
            return []
        return s.split("*space*")