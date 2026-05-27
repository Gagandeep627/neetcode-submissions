class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        # topic : Binary_search:

        
        # Topic : Binary_Search -->
        #To Ensure Nums1 is a smaller array for nums -->

        # topic : binary_search -->
        # enusre nums 1 is the smaller array for binary_search-->
        
        # suppose length of nums 1 is greater length of nums2:
        # have the shortest numsa over the left side:
        # and the largest nums over the rightmost side:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

       

        # m : len(nums1)
        # n : len(nums2)
        # If the smaller array has k elements → binary search takes log(k) steps.
        m, n = len(nums1), len(nums2)
        # total_length : (m + n + 1) // 2
        total_length = (m+n+1) // 2
        # total_length = (m + n)
        # Since k = min(m, n),

        # set lo : 0
        lo = 0
        # set h1 to (m):
        hi = m
        # set i to (0):
        i = 0



        # loop runs untill the (lo <= hi):
        while (lo <= hi):
            # set i : (lo + hi) // 2 : (mid)
            # elements from nums 1 from left
            i = (lo + hi) // 2 #elements from nums1 on left:
            # elements in nums 2 from left:
            j = (total_length - i) #elements from nums2 on left:


            # We perform binary search on only the smaller array (nums1 or nums2).

            # perform binary search : on only the smallere array (like : say nums1 or nums 2)
            

            aleft = nums1[i-1] if i > 0 else float("-inf")

            aright = nums1[i] if (i < m) else float("inf")

            bleft = nums2[j-1] if j > 0 else float("-inf")

            bright = nums2[j] if (j < n) else float("inf")

            # found correct partition:
            if (aleft <= bright and bleft <= aright):
                if ((m+n) % 2): # odd length :
                    return max(aleft, bleft)
                else: #for even length:

                    return (max(aleft, bleft) + min(aright, bright)) / 2.0


            # move search image:
            elif aleft > bright:
                # lo = mid + 1
                # move towards shorter i th value:
                hi = i-1

            else: # if bleft > aright: then move lo to its next positions ujtill bleft < aright:
                lo=i+1
                # hi = mid-1


        # Time = O(log(min(m, n))). : Because:
        # log(min(m, n)) ≤ log(m + n) : This satisfies the NeetCode requirement: O(log(m+n)).
        
        # ✅ Space Complexity : No extra arrays are created.
        # Only a few integer variables and comparisons are used.
        # No recursion or additional data structures.


#         | Operation | Complexity                                            |
# | --------- | ----------------------------------------------------- |
# | **Time**  | ⭐ **O(log(min(m, n)))** → Accepted as **O(log(m+n))** |
# | **Space** | ⭐ **O(1)**                                            |

        return -1


            




        


        

         # Topic : Brute_Force -->

        # set merged : (nums1 + nums2)

        # O(n)
        merged = nums1 + nums2

        # sort the merged nums:-
        # O(nlog(n)) --> O(n) + O(n^log(n)) --> O(n ^ log2(n));
        merged.sort()

        # say n : length of merged nums
        n = len(merged)

        # if suppose n is odd :
        if (n % 2 == 1):
            # then middle element from the nums 
            # will exists which will be defined via float(merged(index : (n // 2)))
            return float(merged[n//2])
        else:
            # evaluate mid 1:
            # mid 1 via : (merged[n//2-1])
            mid1 = merged[n//2 - 1]

            # mid2 via : (merged[n//2])
            mid2 = merged[n//2]

            # answer : (float(mid1 + mid2) / 2.0)
            # return the answer in float value;
            return float((mid1 + mid2) / 2.0) 
        
        


        # Topic : Binary_Search -->
        #To Ensure Nums1 is a smaller array for nums -->

        # topic : binary_search -->
        # enusre nums 1 is the smaller array for binary_search-->
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        lo = 0
        # If the smaller array has k elements → binary search takes log(k) steps.
        m, n = len(nums1), len(nums2)
        total_length = (m+n+1) // 2
        # total_length = (m + n)
        # Since k = min(m, n),
        hi = m
        i = 0




        while (lo <= hi):
            
            i = (lo + hi) // 2 #elements from nums1 on left:
            j = (total_length - i) #elements from nums2 on left:


            # We perform binary search on only the smaller array (nums1 or nums2).

            aleft = nums1[i-1] if i > 0 else float("-inf")

            aright = nums1[i] if (i < m) else float("inf")

            bleft = nums2[j-1] if j > 0 else float("-inf")

            bright = nums2[j] if (j < n) else float("inf")

            # found correct partition:
            if (aleft <= bright and bleft <= aright):
                if ((m+n) % 2): # odd length :
                    return max(aleft, bleft)
                else: #for even length:

                    return (max(aleft, bleft) + min(aright, bright)) / 2.0


            # move search image:
            elif aleft > bright:
                # lo = mid + 1
                # move towards shorter i th value:
                hi = i-1

            else: # if bleft > aright: then move lo to its next positions ujtill bleft < aright:
                lo=i+1
                # hi = mid-1


        # Time = O(log(min(m, n))). : Because:
        # log(min(m, n)) ≤ log(m + n) : This satisfies the NeetCode requirement: O(log(m+n)).
        
        # ✅ Space Complexity : No extra arrays are created.
        # Only a few integer variables and comparisons are used.
        # No recursion or additional data structures.


#         | Operation | Complexity                                            |
# | --------- | ----------------------------------------------------- |
# | **Time**  | ⭐ **O(log(min(m, n)))** → Accepted as **O(log(m+n))** |
# | **Space** | ⭐ **O(1)**                                            |

        return -1


            




        


















        # if (len(nums1) > len(nums2)):
        #     nums1 , nums2 = nums2, nums1
        


        # n1 = len(nums1)
        # n2 = len(nums2)


        # low , high = 0, n1-1


        # while (low <= high):


        #     cut1 =  (low + high) // 2

        #     cut2 = (n1 + n2 + 1) // 2 - cut1




        #     L1 = float("-inf") if cut1 == 0 else nums1[cut1-1]
        #     R1 = float("inf") if cut1 == n1 else nums1[cut1]
        #     L2 = float("-inf") if cut2 == 0 else nums2[cut2-1]
        #     R2 = float("inf") if cut2 == n2 else nums2[cut2]



        #     if (L1 <= R2 and L2 <= R1):

        #         if ((n1 + n2) % 2 == 0):
        #             return (max(L1, L2) + min(R1 , R2)) / 2.0
        #         else:
        #             return float(max(L1, L2))

        #     elif L1 > R2:
        #         high = cut1 - 1
            
        #     else: #L2 > R1
        #         low = cut1 + 1
        



            # topic : Brute Force_solutions :

            # add both nums 1 && nums2 to merged-->

            # .sort() --> merged aray-->

            # n = len(merged)

            # if merged is odd() -- > ans : float(merged[n//2])

            # else: mid1 : merged[n//2-1]
                    # mid2 : merged[n//2]


                    #return ans : float((mid1+mid2) / 2.0)


            




         


