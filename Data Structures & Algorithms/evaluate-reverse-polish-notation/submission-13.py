class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = tokens[0]
        operands = ["+","-","*","/"]

        for t in tokens:
            if t in operands:
                i = int(stack.pop())
                j = int(stack.pop())
                res = eval(f"{j}{t}{i}")
                
                stack.append(int(res))
            else:
                stack.append(t)
        
        return int(res)