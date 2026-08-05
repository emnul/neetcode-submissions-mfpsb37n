# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)
    
    def quickSortHelper(self, pairs, s, e):
        if (e - s) + 1 <= 1:
            return pairs
        
        left = s
        pivotKey = pairs[e].key

        for i in range(s, e):
            if pairs[i].key < pivotKey:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1
        
        pairs[left], pairs[e] = pairs[e], pairs[left]

        self.quickSortHelper(pairs, s, left - 1)
        self.quickSortHelper(pairs, left + 1, e)

        return pairs




