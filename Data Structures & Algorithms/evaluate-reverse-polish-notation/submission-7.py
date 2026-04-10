
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {"+", "-", "*", "/"}
        stack = []
        
        def operation(op,num1,num2):
            if op == "+":
                return num1 + num2
            if op == "-":
                return num1 - num2
            if op == "*":
                return num1 * num2
            if op == "/":
                return int(num1 / num2)
            

        for element in tokens:
            if element not in operations:
                stack.append(int(element))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                answer = operation(element, num1, num2)
                stack.append(answer)
        
        return stack[0]