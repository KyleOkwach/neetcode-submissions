class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                # we have an open bracket
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()  # remove current set of parentheses
            
            if closedN < openN:
                # we have enough open brackets
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res