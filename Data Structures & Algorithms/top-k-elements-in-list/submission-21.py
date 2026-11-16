class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.defaultdict(int) # num to counts
        for num in nums:
            counts[num] += 1

        # use min heap to track k largest
        # nlogk
        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))

            # since min heap pops the smallest elem on each
            # iter, we're left with the top k after processing
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val[1] for val in heap]
