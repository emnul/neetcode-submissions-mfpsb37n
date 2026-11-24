class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curPerm = []
        counts = collections.Counter(nums)

        def dfs():
            if len(curPerm) == len(nums):
                res.append(curPerm[::])
                return
            
            for num in counts:
                if counts[num] > 0:
                    curPerm.append(num)
                    counts[num] -= 1
                    dfs()

                    curPerm.pop()
                    counts[num] += 1
        
        dfs()
        return res