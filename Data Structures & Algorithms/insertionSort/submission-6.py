# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        i = 0
        res = []

        for i in range(len(pairs)):
            left = i - 1
        
            while left >= 0 and pairs[left].key > pairs[i].key:

                pairs[left], pairs[i] = pairs[i], pairs[left]
                left -= 1
                i -= 1
            
            res.append(list(pairs))

        return res
