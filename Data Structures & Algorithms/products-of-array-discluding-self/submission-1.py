class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        prefixProd, postfixProd = ([1] * len(nums) for _ in range(2))
        for i in range(len(nums)):
            prod = prefixProd[i - 1] * nums[i] if i > 0 else nums[i]
            prefixProd[i] = prod
        rightEnd = len(nums) - 1
        print(prefixProd)
        for j in range(len(nums) - 1, -1, -1):
            prod = postfixProd[j + 1] * nums[j] if j < rightEnd else nums[j]
            postfixProd[j] = prod
        print(postfixProd)
        for k in range(len(nums)):
            L = prefixProd[k - 1] if k > 0 else 1
            R = postfixProd[k + 1] if k < rightEnd else 1
            print(L, R)
            out.append(L * R)
        return out