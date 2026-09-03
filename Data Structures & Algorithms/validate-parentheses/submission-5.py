class Solution:
    def isValid(self, s: str) -> bool:
        """

        """ 

        bracket_pair = {"}" : "{", ")" : "(", "]": "["}
        stack = []

        for bracket in s:
            if bracket in bracket_pair:
                if stack and stack[-1] == bracket_pair[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
                
        return True