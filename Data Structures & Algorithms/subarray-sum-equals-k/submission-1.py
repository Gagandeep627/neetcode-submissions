class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        # topic : optimal solutions (hashmap ++ prefixsum approach):


        ps = 0
        c = 0



        pc = {0 : 1}


        for num in nums:

            ps += num


            need = (ps - k)

            if (ps - k) in pc:
                c += pc[ps-k]

            
            if ps not in pc:
                pc[ps] = 1
            else:
                pc[ps] += 1


        ans = c    

        return ans







































































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