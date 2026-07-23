from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        counts = defaultdict(int) # map from num to occurances

        for n in nums:
            counts[n] += 1
        
        for num, count in counts.items():
            bucket[count].append(num)
        
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                for e in bucket[i]:
                    res.append(e)
            
                if len(res) >= k:
                    return res[-k:]