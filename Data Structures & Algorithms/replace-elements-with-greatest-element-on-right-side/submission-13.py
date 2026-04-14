class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        g_elem = arr[len(arr) - 1]
        arr[len(arr) - 1] = -1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] < g_elem:
                arr[i] = g_elem
            else:
                tmp = arr[i]
                arr[i] = g_elem
                g_elem = tmp

        
        return arr