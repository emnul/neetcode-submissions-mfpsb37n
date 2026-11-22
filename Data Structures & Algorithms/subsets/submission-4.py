class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curSubset):
            if i >= len(nums):
                res.append(curSubset.copy())
                return

            # decision to include nums[i]
            curSubset.append(nums[i])
            dfs(i+1, curSubset)

            curSubset.pop()
            # decision not to include subset
            dfs(i+1, curSubset)
            
        
        dfs(0, [])
        return res