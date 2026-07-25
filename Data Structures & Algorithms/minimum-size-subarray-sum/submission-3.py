class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        


        # topic : Optimal Approach solutions (sliding window):-


        # left pointer
        l = 0

        n = len(nums)
        # Current window sum
        window_sum = 0
        # Store minimum length
        min_len = float("inf")

        # expand the window from the rightest end;
        #  The right pointer moves from left to right only once.
        for r in range(0, n):
            
            # add the current element in the window_sum
            window_sum += nums[r]

            # untill window_sum exceeds the target in order to get the minimum possible
            # window with the window_summ >= Target;

            # shrink while the window is valid

            # if the current window sum is at least the target
            # try shrinking teh window from the left to make it as smallas possible
            while (window_sum >= target):

                # update minimum window length
                # update the  minimum window length
                # current window length = (right - left + 1)
                min_len = min((r - l + 1), min_len)

                # update window via removing the leftmost element from the nums
                # remove teh leftmost element from the window
                # since we are shrinking the window
                window_sum -= nums[l]
                
                # increment left pointer by 1 move left pointer 1 step forward;
                l += 1

        # if no valid window was ever found
        # return 0 as required by the problem
        if (min_len == float("inf")):
            return 0

        # Return the length of the smallest valid subarray.
        return min_len

                #  The right pointer moves from left to right only once.
        # The left pointer also moves from left to right only once.
# Time Complexity = O(n)

# Space Complexity = O(1)


            

                

                


        

        
