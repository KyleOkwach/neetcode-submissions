class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += f"{len(s)}#{s}"
        return string

    def decode(self, s: str) -> List[str]:
        pointer = 0
        strs = []

        while pointer < len(s):
            next_pointer = pointer

            while s[next_pointer] != "#":
                next_pointer += 1

            print(s[pointer:], pointer, next_pointer)

            strs.append(s[next_pointer+1:next_pointer + 1 + int(s[pointer:next_pointer])])
            pointer = next_pointer + 1 + int(s[pointer:next_pointer])
        return strs