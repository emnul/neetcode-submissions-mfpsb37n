class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        
        for num in nums:
            if len(res) < k:
                heapq.heappush(res, num)
            else:
                curMin = heapq.heappop(res)
                if curMin < num:
                    heapq.heappush(res, num)
                else:
                    heapq.heappush(res, curMin)
        
        return res[0]