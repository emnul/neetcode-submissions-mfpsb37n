class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Approach: using two pointers we start at each end of the string s.
        # we increment / decrement each pointer until we get to valid alphaNum char
        # we then compare equality of pointers. If not equal not a palin so ret false.
        # else inc / dec pointers and continue loop until pointers pass e/o
        # return true

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            
            while l < r and not s[r].isalnum():
                r -= 1

            
            # pointers may have been updated so we need to check bounds
            if l <= r and s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True
    
