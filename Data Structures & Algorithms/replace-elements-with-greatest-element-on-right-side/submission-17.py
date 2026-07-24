class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxE = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = maxE
            maxE = max(maxE, tmp)
        return arr
