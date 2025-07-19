class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=nums1+nums2
        m.sort()
        mlen=len(m)
        if mlen%2!=0:
            return m[mlen//2]
        else:
            return (m[mlen//2]+m[(mlen//2)-1])/2
        