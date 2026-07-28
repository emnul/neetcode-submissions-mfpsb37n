class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) + "#" + s
        return out


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            # at a # char
            length = int(length)
            decoded = s[i+1:i+1+length]
            res.append(decoded)
            i = i+1+length
        return res

