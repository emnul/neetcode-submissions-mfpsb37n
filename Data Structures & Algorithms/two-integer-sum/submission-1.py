class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            ith = nums[i]
            for j in range(i+1, len(nums)):
                jth = nums[j]
                if ith + jth == target:
                    return [i, j]
                
        