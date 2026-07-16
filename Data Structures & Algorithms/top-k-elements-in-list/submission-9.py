from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        print(buckets)
        counts = Counter(nums) # mapping from item -> freq
        for item, freq in counts.items():
            buckets[freq].append(item)
        
        ret = []
        for i in range(len(buckets) - 1, -1, -1):
            ret += buckets[i]
            if len(ret) >= k:
                return ret[0:k]
                

            