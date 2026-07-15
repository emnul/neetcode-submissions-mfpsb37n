class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            val = nums[i]
            j = hm.get(target - val)
            if j != None and i < j:
                return [i, j]
            elif j != None:
                return [j, i]
            hm[val] = i
