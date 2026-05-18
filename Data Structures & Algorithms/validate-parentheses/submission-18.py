class Solution:
    def isValid(self, s: str) -> bool:
        # invalid if odd num
        if len(s) % 2 == 1 or len(s) < 2:
            return False

        stack = []
        for i in s:
            # push open brackets to stack
            if i == "(":
                stack.append(i)
            elif i == "{":
                stack.append(i)
            elif i == "[":
                stack.append(i)
            else:
                # check if stack is empty
                if not stack:
                    return False

                # closing bracket must match top of stack
                a = stack.pop()
                
                if a == "(" and i != ")":
                    return False
                elif a == "{" and i != "}":
                    return False
                elif a == "[" and i != "]":
                    return False
        
        if stack:
            return False
            
        return True