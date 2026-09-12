class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        operators = ["+", "-", "/", "*"]
        stack = []
        res = 0
        for val in tokens:
            # print("stack: ", stack)
            if val in operators:
                # print("operator entered in cal loop: ", val)
                t = int(stack.pop()) # pop first val
                # print("pop: ", pop)
                # print("current res: ", res)
                match val:
                    case "+":
                        res = int(stack.pop()) + t  # cal with 2nd val
                    case "-":
                        res = int(stack.pop()) - t # cal with 2nd val
                    case "*":
                        res = int(stack.pop()) * t # cal with 2nd val
                    case "/":
                        res = int(int(stack.pop()) / t) # cal with 2nd val
                
                # print("res: ", res)
                stack.append(res)
                # print("stack after cals: ",stack)
                continue
            
            # otherwise push to stack 
            stack.append(val)
        
        return stack[-1]