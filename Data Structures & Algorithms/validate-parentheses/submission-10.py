class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesPairs = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for p in s:
            if p in parenthesesPairs:
                if stack and stack[-1] == parenthesesPairs[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return not stack