# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        out = []
        if not pairs:
            return out
        out.append(list(pairs))
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                # swap pair
                tmp = pairs[j]
                pairs[j] = pairs[j + 1]
                pairs[j + 1] = tmp
                j -= 1
            out.append(list(pairs))
        return out
