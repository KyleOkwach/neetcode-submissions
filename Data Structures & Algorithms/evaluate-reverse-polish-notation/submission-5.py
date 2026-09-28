class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        num_buffer = []

        for t in tokens:
            if t not in operators:
                num_buffer.append(t)
            else:
                res = self.evalStack(int(num_buffer[-2]), int(num_buffer[-1]), t)
                num_buffer.pop()
                num_buffer.pop()
                num_buffer.append(int(res))
        
        return int(num_buffer[0])
    
    def evalStack(self, a, b, op) -> int:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b