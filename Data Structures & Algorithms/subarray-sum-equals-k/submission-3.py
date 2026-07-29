class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        # topic : optimal solutions (hashmap ++ prefixsum approach):

        # stores the running (Prefix) sum
        ps = 0
        # stores the total no.s of valid subarrays.
        c = 0


        # hashmap : {prefixsum : frequency}
        # initially prefix sum 0 has occured once.
        # this handles subarrays starting from index : 0
        pc = {0 : 1}

# traverse every element in the array
# each element is processed once, and hash map operations are O(1) on average.
        for num in nums:
            
            # update the current prefix sum
            ps += num

            # if the (prefixsum-k) exists.
            # then a subarray ending at the current index has sum == k.
            need = (ps - k)

            if (ps - k) in pc:

                # add all occurences accdn. to the need (prefixsum - k) bcz the 
                # because the same prefix sum may have appeared multiple times.
                c += pc[ps-k]

            # store and update the frequency of the current prefix sum.
            if ps not in pc:
                pc[ps] = 1
            else:
                pc[ps] += 1

        # return the total no. of valid subarrays.
        ans = c    

        return ans




#         answer = 0

# prefixSum = 0

# Create hashmap

# hashmap[0] = 1

# For every number

#     prefixSum += number

#     If (prefixSum - k) exists
#           answer += hashmap[prefixSum-k]

#     Store current prefixSum

# Return answer

#         Time: O(n) — each element is processed once, and hash map operations are O(1) on average.
# Space: O(n) — in the worst case, we store up to n + 1 distinct prefix sums.







































































        # # topic : brute force solutions : O(N ^2):


        # ans = 0

        # n = len(nums)

        # # O(n)
        # for s in range(0, n):
            
        #     curr_sum = 0

        #     # O(n)
        #     for e in range(s, n):

        #         curr_sum += nums[e]

        #         if (curr_sum == k):
        #             ans += 1

        # # time complexity : O(n * n) : O(n ^ 2);
        # return ans