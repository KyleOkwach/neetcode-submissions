class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_arr = list([a.lower() for a in s if a.isalnum()])
        return alnum_arr == alnum_arr[::-1]