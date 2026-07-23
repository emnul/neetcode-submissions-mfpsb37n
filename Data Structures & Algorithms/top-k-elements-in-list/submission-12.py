from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        counts = defaultdict(int) # map from num to occurances

        for n in nums:
            counts[n] += 1
            bucket[counts[n]].append(n)
        
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                for e in bucket[i]:
                    if e not in res:
                        res.append(e)
            
                if len(res) >= k:
                    return res[-k:]