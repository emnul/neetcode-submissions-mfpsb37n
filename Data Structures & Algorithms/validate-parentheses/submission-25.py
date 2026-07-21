class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping from closing bracket to open bracket
        bracketMap = {"}": "{", "]": "[", ")": "("}

        for char in s:
            # Add opening brackets to stack
            if char not in bracketMap:
                stack.append(char)
            else:
                # Check for empty stack
                if not stack:
                    return False
                else:
                    openB = stack.pop()
                    if bracketMap[char] != openB:
                        return False
        
        return True if not stack else False

