class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            # at a leaf node when i == len(nums)
            if i >= len(nums):
                res.append(subset[:]) # we only care about leaf nodes, need to make a copy
                return
            
            # case where we choose to append val at i
            subset.append(nums[i])
            dfs(i+1)

            # case where we choose NOT to append
            subset.pop()
            dfs(i+1)
            
            
        dfs(0)
        return res