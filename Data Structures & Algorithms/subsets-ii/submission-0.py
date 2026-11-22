class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(i, curSubset):
            if i >= len(nums):
                res.append(curSubset.copy())
                return
            
            # decision to include nums[i]
            curSubset.append(nums[i])
            dfs(i+1, curSubset)

            # backtrack
            curSubset.pop()
            
            # decision to not include nums[i]
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, curSubset)
        
        dfs(0, [])
        return res