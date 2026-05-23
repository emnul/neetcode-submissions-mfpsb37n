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

        kMostFreq = []
        i = len(buckets) - 1
        while k and i >= 0:
            bucket = buckets[i]
            for item in bucket:
                kMostFreq.append(item)
                k -= 1
            i -= 1
            
        return kMostFreq
            
        