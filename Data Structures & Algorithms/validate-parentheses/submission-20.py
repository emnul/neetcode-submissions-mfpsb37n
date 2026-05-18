class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            # pop from stack if stack not empty, c is closing and 
            if stack and c in closeToOpen:
                # top of stack should match closing paren
                if stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        # stack should be empty ex "{{{" would not return False 
        return True if not stack else False