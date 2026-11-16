class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1

        # we can have at most len occurances so we need len + 1 buckets
        # bucket ind maps to count of elem
        buckets = [[] for _ in range(len(nums) + 1)]

        # add each val to appropriate bucket
        for val, count in counts.items():
            buckets[count].append(val)
                    
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            for val in bucket:
                res.append(val)

                if len(res) == k:
                    return res
        

        


