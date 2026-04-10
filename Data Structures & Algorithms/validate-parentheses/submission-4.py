class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {"}" : "{", "]" : "[", ")" : "("}
        stack = []

        for parentheses in s:
            if parentheses in bracketMap:
                if not stack:
                    return False
                else:
                    if bracketMap[parentheses] == stack[-1]:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(parentheses)

        if stack:
            return False
        else:
            return True