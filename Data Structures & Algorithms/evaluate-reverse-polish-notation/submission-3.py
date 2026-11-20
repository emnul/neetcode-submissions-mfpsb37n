class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        stack = []
        while i < len(tokens):
            if tokens[i] == "+":
                op2, op1 = stack.pop(), stack.pop()
                result = int(op1) + int(op2)
                stack.append(result)
            elif tokens[i] == "-":
                op2, op1 = stack.pop(), stack.pop()
                result = int(op1) - int(op2)
                stack.append(result)
            elif tokens[i] == "*":
                op2, op1 = stack.pop(), stack.pop()
                result = int(op1) * int(op2)
                stack.append(result)
            elif tokens[i] == "/":
                op2, op1 = stack.pop(), stack.pop()
                result = int(op1 / op2)
                stack.append(result)
            else:
                stack.append(int(tokens[i]))
            i += 1
        
        return stack[0]