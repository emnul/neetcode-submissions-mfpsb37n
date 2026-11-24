class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = collections.Counter(nums)

        perm = []
        res = []
        def permute():
            if len(perm) == len(nums):
                res.append(perm[::])
                return
            
            for n in counts:
                if counts[n] > 0:
                    counts[n] -= 1
                    perm.append(n)
                    permute()

                    counts[n] += 1
                    perm.pop()
        permute()
        return res