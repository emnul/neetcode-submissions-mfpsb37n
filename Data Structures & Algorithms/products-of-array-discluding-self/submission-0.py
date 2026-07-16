from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)): # calc product skip over i
                if j != i:
                    prod *= nums[j]
            out.append(prod)
        return out

        