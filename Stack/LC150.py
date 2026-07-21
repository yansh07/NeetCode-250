# Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: list[str])-> int:
        stack = []
    
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # Pop the second operand first due to stack LIFO ordering
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Truncate division toward zero
                    stack.append(int(a / b))
            else:
                # Token is an integer, push it to the stack
                stack.append(int(token))
                
        return stack[0]


s = Solution()
print(s.evalRPN( tokens = ["2","1","+","3","*"]))