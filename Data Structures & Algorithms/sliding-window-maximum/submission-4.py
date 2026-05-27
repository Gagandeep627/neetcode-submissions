
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        #topic : sliding window -->


        


        dq = deque() # stores indexes of useful elements


        result = []



        for i in range(len(nums)):

            # 1️⃣ Remove indexes that are out of the current window
            while dq and dq[0] <= i - k:
                dq.popleft()


            
            
            # 2️⃣ Remove smaller elements from the right end
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3️⃣ Add the current element’s index
            dq.append(i)

            # 4️⃣ Once we have the first full window, record the max
            if (i  >= k - 1) and dq:
                result.append(nums[dq[0]])  # the element at front is max


        

        return result 
























        # Topic : Brute Force Solution Concept for Solving the problem.. ++ : ++ ??
        # result = []
        # # O(n - k + 1) : O(k) th iterations -->
        # for i in range(len(nums) - k + 1):
        #     # O(i -> i + 3) : O(n will concatinate once all elements in the sub_list)
            
        #     window = nums[i : i + k]
        #     # O(n)
        #     window_max = max(window)
        #     result.append(window_max)

        # #time_complexity : O(n * k). ++ : ++ ??
        # return result
        