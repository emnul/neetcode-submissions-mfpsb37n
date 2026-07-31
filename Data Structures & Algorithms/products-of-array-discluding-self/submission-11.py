class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)

        preProd = 1
        for i in range(len(nums)):
            out[i] = preProd
            preProd *= nums[i]
        
        postProd = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= postProd
            postProd *= nums[i]
        
        return out