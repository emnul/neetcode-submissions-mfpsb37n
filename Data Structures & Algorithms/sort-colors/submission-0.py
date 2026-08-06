class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3
        for color in nums:
            buckets[color] += 1
        
        ind = 0
        for i in range(len(buckets)):
            for _ in range(buckets[i]):
                nums[ind] = i
                ind += 1