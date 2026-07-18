class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # Compute prefix product
        prefixProd = 1
        for i in range(len(nums)):
            prefixProd = res[i - 1] if i > 0 else 1
            res[i] = prefixProd * nums[i - 1] if i > 0 else prefixProd * 1
        # Compute postfix product
        postfixProd = 1
        for j in range(len(nums) - 1, -1, -1):
            postfixProd = nums[j + 1] * postfixProd if j < len(nums) - 1 else 1
            res[j] *= postfixProd
        return res
        