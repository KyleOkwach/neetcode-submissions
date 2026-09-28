class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        num_buffer = []

        for t in tokens:
            if t not in operators:
                num_buffer.append(t)
            else:
                b = int(num_buffer.pop())
                a = int(num_buffer.pop())
                res = self.evalAB(a, b, t)
                num_buffer.append(int(res))
        
        return int(num_buffer[0])
    
    def evalAB(self, a, b, op) -> int:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b