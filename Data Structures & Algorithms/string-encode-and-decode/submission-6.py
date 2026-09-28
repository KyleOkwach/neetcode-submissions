class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in range(len(strs)):
            out += f"{strs[s]};"

        return out

    def decode(self, s: str) -> List[str]:
        out, tmp = [], ''
        
        for c in s:
            if c == ';':
                out.append(tmp)
                tmp = ''
                continue
            else:
                tmp += c
                continue
            

        return out