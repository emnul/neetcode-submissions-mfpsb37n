class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # we can use sorted property of array to simplify problem to 2 Sum 

        for i in range(len(nums)):
            # We've already found all triplets that start with i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # use two ptr technique to find all triplets that start with nums[i]
            # bc the array is now sorted we can find all valid triplets in a single pass
            l,r = i+1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    # found match so move l to first val not equal to self
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res
                    

            
