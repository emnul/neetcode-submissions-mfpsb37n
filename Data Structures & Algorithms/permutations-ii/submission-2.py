class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        counts = collections.Counter(nums)

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm[::])
                return

            for n in counts:
                if counts[n] > 0:
                    perm.append(n)
                    counts[n] -= 1

                    backtrack()

                    counts[n] += 1
                    perm.pop()
        
        backtrack()
        return res