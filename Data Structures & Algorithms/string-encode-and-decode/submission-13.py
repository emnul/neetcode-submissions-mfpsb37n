class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s)) + "_" + s
        return enc 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "_":
                j += 1
            length = int(s[i:j])
            dec = s[j+1:j+1+length]
            res.append(dec)
            i = j + 1 + length
        return res

