class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        


        # topic : brute force solutions:-

        n = len(nums)

         # Store the minimum length found
        min_len = float("inf")


        # Outer loop: n times. O(n)

        # try every starting index
        for i in range(0, n):
            
            # sum of current subarray
            curr = 0

            # Inner loop: Up to n times. O(n)

            # extend the subarray
            for j in range(i, n):
                
                # sum of current subarray
                curr += nums[j]


                # if the curr_sum is reached the target 
                if (curr >= target):
                    

                    # lengt of current subarray
                    length = (j - i + 1)


                    # update minimum length
                    min_len = min(min_len, length)


                    # no need to check the longer subarrays
                    break


        # time : o(n * n) : O(n ^ 2);
        # Space Complexity: O(1)

        # if no valid subarray is found:
        if (min_len == float("inf")):
            return 0

        return min_len
