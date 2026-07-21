class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # push left brackets onto stack
        # pop when we see right bracket
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")" or char == "}" or char == "]":
                # Return false if stack is empty
                if not stack:
                    return False
                # Check that brackets match
                else:
                    b = stack.pop()
                    if char == ")" and b != "(":
                        return False
                    elif char == "}" and b != "{":
                        return False
                    elif char == "]" and b != "[":
                        return False
        
        # check if stack still has items
        print(stack)
        if stack:
            return False
        else:
            return True
                
