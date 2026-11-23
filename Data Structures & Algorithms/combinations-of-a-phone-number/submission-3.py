class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        digitsToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i, curComb):
            if len(curComb) == len(digits):
                res.append(curComb)
                return
            if i == len(digits):
                return
            
            for c in digitsToLetters[digits[i]]:
                dfs(i+1, curComb + c)
        
        dfs(0, "")
        return res