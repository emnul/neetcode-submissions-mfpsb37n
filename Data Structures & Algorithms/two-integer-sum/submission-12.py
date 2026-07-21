class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToInd = {}

        for currI, val in enumerate(nums):
            sol = target - val
            if sol not in valToInd:
                valToInd[val] = currI
            else:
                return [valToInd[sol], currI]
            
