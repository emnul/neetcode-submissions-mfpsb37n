class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curComb, curSum):
            if curSum > target or i >= len(nums):
                return
            if curSum == target:
                res.append(curComb[::])
                return
            
            # choose current num
            curComb.append(nums[i])
            dfs(i, curComb, curSum + nums[i])
            curComb.pop()
            
            # don't choose cur num
            dfs(i+1, curComb, curSum)

        dfs(0, [], 0)
        return res