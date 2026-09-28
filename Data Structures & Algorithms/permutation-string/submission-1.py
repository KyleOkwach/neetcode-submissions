class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0 + len(s1)
        counter = {char: s1.count(char) for char in s1}

        while r < len(s2) + 1:
            curr = {char: s2[l:r].count(char) for char in s2[l:r]}
            print(s1, s2[l:r], counter, curr)
            if counter == curr:
                return True
            l += 1
            r += 1
        
        return False
