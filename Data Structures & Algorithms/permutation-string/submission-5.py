class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        counter = [0] * 26
        curr = [0] * 26
        
        # Count frequencies
        for c in s1:
            counter[ord(c) - ord('a')] += 1

        for ri, r in enumerate(s2):
            curr[ord(r) - ord('a')] += 1
            li = ri-len(s1)+1
            l = s2[li]
            if li >= 0:
                if counter == curr:
                    return True
                curr[ord(l) - ord('a')] -= 1
        
        return False
