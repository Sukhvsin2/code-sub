class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        operators = ["+", "-", "/", "*"]
        stack = []
        res = 0
        for val in tokens:
            if val in operators:
                t = int(stack.pop()) # pop first val
                match val:
                    case "+":
                        res = int(stack.pop()) + t  # cal with 2nd val
                    case "-":
                        res = int(stack.pop()) - t # cal with 2nd val
                    case "*":
                        res = int(stack.pop()) * t # cal with 2nd val
                    case "/":
                        res = int(int(stack.pop()) / t) # cal with 2nd val
                
                stack.append(res)
                continue
            
            # otherwise push to stack 
            stack.append(val)
        
        return stack[-1]