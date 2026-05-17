class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {val: idx for idx, val in enumerate(nums)}
        print(hm)
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in hm and hm[diff] != i:
                return [i, hm[diff]]

                
        