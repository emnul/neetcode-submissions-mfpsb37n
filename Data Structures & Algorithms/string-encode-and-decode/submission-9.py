class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            # need 2 ptrs to determine len value
            j = i
            # we reach end of int vals when we hit delim
            while s[j] != "#":
                j += 1
            # get encoded length
            length = int(s[i:j])
            
            res.append(s[j+1:j+1+length])
            # update i pointer
            i = j + 1 + length
               

        return res






