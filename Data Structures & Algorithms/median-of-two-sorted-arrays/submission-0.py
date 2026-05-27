class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        



        # Topic : Brute_Force -->


        merged = nums1 + nums2


        merged.sort()


        n = len(merged)


        if (n % 2 == 1):
            return float(merged[n//2])
        else:
            mid1 = merged[n//2 - 1]

            mid2 = merged[n//2]


            return float((mid1 + mid2) / 2.0) 