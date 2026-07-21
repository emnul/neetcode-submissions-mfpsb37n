class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingMap = {")": "(", "}": "{", "]": "["}

        for c in s:
            # Check for open paren
            if c not in closingMap:
                stack.append(c)
            else:
                # check for empty stack
                if not stack:
                    return False
                elif stack[-1] != closingMap[c]:
                    return False
                else:
                    stack.pop()
        
        return False if stack else True
