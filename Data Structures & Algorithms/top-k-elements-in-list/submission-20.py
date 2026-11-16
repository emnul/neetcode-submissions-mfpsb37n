class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.defaultdict(int) # value to freq
        for num in nums:
            freqs[num] += 1
        
        # {1: 1, 2: 3, 3: 4}
        sortedFreqs = sorted([(count, val) for val, count in freqs.items()])
        return [val[1] for val in sortedFreqs[-k:]]
        
