class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
#approach
#iterate over the tokens, until you find an operand.
#perform that operand on the last two in the stack
#at the end of the day return the el @ zeroth index of stack
        ops = {"+", "-", "/", "*"}
        stack = []

        for i in range(len(tokens)):
            curr = tokens[i]
            if curr in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                if curr == "+":
                    stack.append(num1 + num2)
                elif curr == "-":
                    stack.append(num1 - num2)
                elif curr == "/":
                    stack.append(int(num1 / num2))
                elif curr == "*":
                    stack.append(num1 * num2)
            else:
                stack.append(int(curr))
        
        return stack[0]
        