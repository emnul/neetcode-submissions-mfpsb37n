class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        def canEat(k):
            totalHrs = 0
            for num in piles:
                totalHrs += math.ceil(num / k)
            return totalHrs <= h

        while (l <= r):
            m = (l + r) // 2

            e = canEat(m)

            if e:
                r = m - 1
                k = min(k, m)
            else:
                l = m + 1
        
        return k


        




