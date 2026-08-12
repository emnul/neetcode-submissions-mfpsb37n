class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = collections.Counter(nums)
        for v, count in counts.items():
            buckets[count].append(v)
        
        res = []
        i = len(buckets) - 1
        while True:
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
            i -= 1
                    

