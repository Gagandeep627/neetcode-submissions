class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        memo = {}
        # topic : recursive ++ memoization (top-down-dp-solutions)-->

        # if (n == 0): return 0;(no elements in nums)-->
        if (n < 1):
            return 0
        # if (n == 1): return nums[index : 0]-->
        if (n == 1):
            return nums[0]


        def helper(nums, i, memo):
            
            # base case 1: if (i >= len(nums)):ans --> 0;
            if (i >= len(nums)):
                return 0
            # if index present in the memo
            # return result store there rather than calculating same results again and again.
            if (i in memo):
                return memo[i]

            # for curr_rob --> include nums[i] and skip nums[i+1]
            # and then raise the helper_function(index--> (i + 2))-->
            curr_rob = (nums[i] + helper(nums,i + 2, memo))
            
            # exclude the current nums[i] and move to
            # then include the next no. and exclude the current nums[i]-->
            skip_rob = (helper(nums, i + 1, memo))

            # store max(current_rob, skip_rob) --> to the memo[i] 
            # -> return memo[i] ->
            memo[i] = max(curr_rob, skip_rob)

            return memo[i]

            
        


        
        # as houses are cyclic so taking whole nums will damage --> 
        # the concept of helper function with length for odd and even by our both 
        # curr_rob && skip_rob pointers --> 
        # so better to exculde the over lapping the results of the 
        # 1st and 2 nd house better isn to
        # once in case 1: exclude -> first house-->
        case1 = helper(nums[:n-1], 0, {})

        # in case 2: exclude --> last house-->
        case2 = helper(nums[1:n], 0, {})


                                  
        # return max(case1, case2) --> will gives max cost while collecting
        # cost from each nums[i] excluding the cyclicity of nums
        # i.e --> first house(case 1), 
        # last house (case 2)
        return max(case1, case2)




            



        