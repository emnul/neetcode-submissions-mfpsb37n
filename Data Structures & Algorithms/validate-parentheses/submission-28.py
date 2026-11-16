class Solution:
    def isValid(self, s: str) -> bool:
        rToL = {'}': '{', ']': '[', ')': '('}
        stack = []

        i = 0
        while i < len(s):
            # push to stack if l paren
            if s[i] not in rToL:
                stack.append(s[i])
            # pop if equiv closing paren at top of stack
            elif stack and stack[-1] == rToL[s[i]]:
                stack.pop()
            else:
                return False
            
            i += 1
        
        # check for edge case eg "(("
        if not stack:
            return True
        else:
            return False