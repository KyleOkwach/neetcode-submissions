class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        num_buffer = []

        for t in tokens:
            if t not in operators:
                num_buffer.append(t)
            else:
                res = eval(f"{num_buffer[-2]}{t}{num_buffer[-1]}")
                num_buffer.pop()
                num_buffer.pop()
                num_buffer.append(int(res))
        
        return int(num_buffer[0])
        