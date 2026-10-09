class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        combo = []
        def dfs(i, curSum):
            if i >= len(nums) or curSum >= target:
                if curSum == target:
                    res.append(combo[:])
                return
            
            # continue exploring nums[i]
            combo.append(nums[i])
            dfs(i, curSum + nums[i])

            # investigate nums[i + 1] branch
            combo.pop()
            dfs(i + 1 , curSum)
            

        dfs(0, 0)
        return res