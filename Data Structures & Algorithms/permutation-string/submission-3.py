class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = [0] * 26
        curr = [0] * 26
        
        # Count frequencies
        for c in s1:
            counter[ord(c) - ord('a')] += 1
        # for c in s2[l:len(s1)]:
        #     curr[ord(c) - ord('a')] += 1

        for ri, r in enumerate(s2):
            curr[ord(r) - ord('a')] += 1
            li = ri-len(s1)+1
            l = s2[li]
            print(s1, s2[li:ri+1], counter, curr)
            if li >= 0:
                if counter == curr:
                    return True
                curr[ord(l) - ord('a')] -= 1
        
        return False
