class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {"(": ")", "{": "}", "[": "]"}

        for bracket in s:
            if bracket in openToClose:
                stack.append(bracket)
            elif bracket not in openToClose and stack:
                open = stack.pop()
                if openToClose[open] != bracket:
                    return False
            else:
                return False
        
        if stack:
            return False
        return True
