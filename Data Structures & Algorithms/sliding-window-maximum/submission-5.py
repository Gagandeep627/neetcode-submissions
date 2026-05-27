
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        #topic : sliding window -->


        


        dq = deque() # stores indexes of useful elements


        result = []


        # time_complexity : O(N) : each elements is scanned only once will be 
        # its optimal approach to resoilve the question with the method of the sliding 
        #window concept.. : //
        for i in range(len(nums)):

            # 1️⃣ remove that indices that are out of the current window that is : (i - k) when index is 
            # equal to (i - k) or less than it means it is from the previous window so remove that element from that index
            #of the window..
            while dq and dq[0] <= i - k:
                dq.popleft()


            
            
            # 2️⃣  then at the last index of the dq if the number of it is < nums[i] then remove it from
            #dq so that only larger values at the right side of the dq exists so remove that
            #last index from the dq -->
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3️⃣ Add teh current element's index to the deque..
            dq.append(i)

            # 4️⃣ once i has exceed the >= k - 1 length and dq existed then record the value of that index in nums 
            #to store the highest possible value's in the list(result) --> 
            if (i  >= k - 1) and dq:
                result.append(nums[dq[0]])  # the element at the front is max -->


        
        # return the resultant ans -->
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
        