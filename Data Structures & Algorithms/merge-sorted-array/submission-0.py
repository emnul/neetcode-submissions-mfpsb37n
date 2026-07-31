class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = k = 0
        l = nums1[:m]
        while i < len(l) and j < len(nums2):
            if l[i] <= nums2[j]:
                nums1[k] = l[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        while i < len(l):
            nums1[k] = l[i]
            i += 1
            k += 1
        
        while j < len(nums2):
            nums1[k] = nums2[j]
            j += 1
            k += 1