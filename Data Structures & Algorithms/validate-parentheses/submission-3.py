class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict ={"}" : "{", "]" : "[", ")" : "("}
        stack = []

        for bracket in s:
            if bracket not in valid_dict:
                stack.append(bracket)
            else:
                if not stack or stack.pop() != valid_dict[bracket]:
                    return False
        
        return len(stack) == 0