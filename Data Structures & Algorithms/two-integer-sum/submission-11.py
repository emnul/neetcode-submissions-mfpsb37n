class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToInd = {val: ind for ind, val in enumerate(nums)}

        for currI, val in enumerate(nums):
            sol = target - val
            if sol in valToInd and currI != valToInd[sol]:
                return [min(currI, valToInd[sol]), max(currI, valToInd[sol])]
            
