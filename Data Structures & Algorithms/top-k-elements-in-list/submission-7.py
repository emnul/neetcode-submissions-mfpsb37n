from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if counter isnt allowed we can just use dict with a mapping
        # from num to count and iterate over the original list to get the
        # count
        counts = Counter(nums)
        # must use list comprehension in Python to create a list of independent sublists
        # / distinct Lists in memory. The multiplication approach eg [[]] * n creates a shared
        # reference to the same list object
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
        return res
            
        