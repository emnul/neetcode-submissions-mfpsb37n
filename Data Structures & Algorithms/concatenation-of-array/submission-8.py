class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans.extend(nums)
        for i in range(len(nums)):
            ans.append(nums[i])

        return ans