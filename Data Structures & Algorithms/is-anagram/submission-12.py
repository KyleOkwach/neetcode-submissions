class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(s, reverse=True)) == "".join(sorted(t, reverse=True))
        