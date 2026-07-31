# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        # sort left and right half of the array
        mid = len(pairs) // 2
        l = self.mergeSort(pairs[:mid])
        r = self.mergeSort(pairs[mid:])

        # merge sorted subarrays into original arr
        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i].key <= r[j].key:
                pairs[k] = l[i]
                i += 1
                k += 1
            else:
                pairs[k] = r[j]
                j += 1
                k += 1

        while i < len(l):
            pairs[k] = l[i]
            i += 1
            k += 1
        
        while j < len(r):
            pairs[k] = r[j]
            j += 1
            k += 1

        return pairs