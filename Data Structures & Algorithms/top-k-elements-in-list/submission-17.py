class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countBuckets = [[] for _ in range(len(nums) + 1)]
        countMap = collections.defaultdict(int) # num -> count
        for num in nums:
            countMap[num] += 1
        # [[], [1], [2], [3]]
        for num, count in countMap.items():
            countBuckets[count].append(num)
        res = []
        for idx in range(len(countBuckets) - 1, -1, -1):
            for item in countBuckets[idx]:
                res.append(item)
                if len(res) == k:
                    return res
        