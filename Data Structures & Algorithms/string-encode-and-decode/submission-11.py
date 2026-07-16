class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            encoded_s += "_" + str(len(s)) + "_" + s
        return encoded_s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i] == '_':
                length = ''
                i += 1
                while s[i] != '_':
                    length += s[i]
                    i += 1
                if i + 1 < len(s):
                    orig_s = s[(i+1):(i+1+int(length))]
                    res.append(orig_s)
                    i += 1 + int(length)
                else:
                    res.append("")
                    break
        return res
