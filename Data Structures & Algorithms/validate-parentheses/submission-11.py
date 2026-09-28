class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        bracket_pairs = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }
        for p in s:
            if p in bracket_pairs:
                if stack and stack[-1] == bracket_pairs[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return not stack