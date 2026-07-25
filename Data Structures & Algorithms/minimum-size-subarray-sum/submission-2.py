class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        


        # topic : Optimal Approach solutions (sliding window):-



        l = 0

        n = len(nums)

        window_sum = 0

        min_len = float("inf")


        for r in range(0, n):

            window_sum += nums[r]

            # untill window_sum exceeds the target in order to get the minimum possible
            # window with the window_summ >= Target;
            while (window_sum >= target):

                # update minimum window length
                min_len = min((r - l + 1), min_len)

                # update window via removing the leftmost element from the nums
                window_sum -= nums[l]
                
                # increment left pointer by 1
                l += 1

        if (min_len == float("inf")):
            return 0

        return min_len
        



            

                

                


        

        
