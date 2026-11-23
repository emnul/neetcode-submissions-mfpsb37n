class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        numToLetters = {
                str(i): [] for i in range(2,10)
            }
                
        k = 0
        for i in range(2,7):
            for j in range(3):
                numToLetters[str(i)].append(chr(ord('a') + k))
                k += 1
        numToLetters['7'] = ['p', 'q', 'r', 's']
        numToLetters['8'] = ['t', 'u', 'v']
        numToLetters['9'] = ['w', 'x', 'y', 'z']


        def dfs(i, curComb):
            if len(curComb) == len(digits):
                res.append("".join(curComb))
                return
            if i >= len(digits):
                return
            
            curNum = digits[i]
            possibleNums = numToLetters[curNum]
            for j in range(len(possibleNums)):
                curComb.append(possibleNums[j])
                dfs(i+1, curComb)
                curComb.pop()
        
        dfs(0, [])
        return res