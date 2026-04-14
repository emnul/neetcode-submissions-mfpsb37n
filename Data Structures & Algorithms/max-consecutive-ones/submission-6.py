class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                if count > max:
                    max = count
                count = 0

        if count > max:
            max = count
            
        return max
        