class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        window, t_counter = [0] * 52, [0] * 52
        have, need = 0, 0
        res, reslen = [-1, -1], float("infinity")
        l = 0

        for c in t:
            if t_counter[ord('a') - ord(c)] <= 0:
                need += 1
            t_counter[ord('a') - ord(c)] += 1

        
        for r in range(len(s)):
            curr = ord('a') - ord(s[r])
            window[curr] += 1

            if t_counter[curr] > 0 and window[curr] == t_counter[curr]:
                have += 1
            
            while have == need:
                # update result
                curr_l = ord('a') - ord(s[l])
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = (r - l + 1)
                # pop from left of window
                window[curr_l] -= 1
                if t_counter[curr_l] > 0 and window[curr_l] < t_counter[curr_l]:
                    have -= 1
                l += 1


        l, r = res
        return s[l: r+1] if reslen != float("infinity") else ""
