class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1
        sortedArr = []
        for n, c in counts.items():
            sortedArr.append((c, n))
        sortedArr.sort()
        res = []
        for i in range(len(sortedArr) -1 , -1, -1):
            res.append(sortedArr[i][1])
            if len(res) == k:
                return res
