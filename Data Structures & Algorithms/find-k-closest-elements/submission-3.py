class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:


           # topic : Optimal Approach solutions (sliding window):-
        # Smallest possible starting index of the window
        l = 0
        # Largest possible starting index of the window
        r = len(arr) - k

        # O(log(n - k))

        # binary search to find the best window
        while (l < r):
            
            # middele starting index of the current search space
            m = (l + r) // 2

        #    compare
        # distance of the leftmost elemenr of the current window from the x
        # with
        # distance of the next element (outside the window)from x
            if (x - arr[m]) > (arr[m+k] - x):

                # left element is farther so , move the window to the right
                l = m + 1

            else:

                # curr window is better (or tie) keep searching for left
                r = m
        # O(k)

        # return the k elements startig from the last window
        ans = arr[l : l + k]


        # time : O(log(n - k) + k)

        # O(1) (excluding the returned list)
        return ans




