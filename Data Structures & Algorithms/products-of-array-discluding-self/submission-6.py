class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # Compute prefix product
        prefixProd = 1
        for i in range(len(nums)):
            res[i] = prefixProd
            prefixProd *= nums[i]
        # Compute postfix product
        postfixProd = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfixProd
            postfixProd *= nums[i]
        return res
        