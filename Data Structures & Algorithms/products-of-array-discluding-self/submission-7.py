class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefixProd = 1
        for i in range(len(nums)):
            res[i] = prefixProd
            prefixProd *= nums[i]
        
        postfixProd = 1
        for i in range(len(nums) - 1, -1 , -1):
            res[i] *= postfixProd
            postfixProd *= nums[i]
        
        return res