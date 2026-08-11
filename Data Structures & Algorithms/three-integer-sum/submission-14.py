class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1
                    # avoid duplicate 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
        return res
