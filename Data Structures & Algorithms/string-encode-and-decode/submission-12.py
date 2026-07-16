class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            encoded_s += str(len(s)) + "_" + s
        return encoded_s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "_":
                j += 1
            length = int(s[i:j])
            orig_s = s[j+1 : j+1+length]
            res.append(orig_s)
            i = j + 1 + length

        return res
