class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        
        # topic : recursive ++ memoizations solutions-->


        total = sum(nums)

        if (total % 2 != 0):
            return False

        target = total // 2

        memo = {}

        def recurse(i, currsum):


            if (currsum == target):
                return True
            
            if (i == len(nums) or (currsum > target)):
                return False


            if (i, currsum) in memo:
                return memo[(i,currsum)]

            # option 1 : take-->
            take = recurse(i + 1, currsum + nums[i])


            skip = recurse(i + 1, currsum)


            if (take):
                memo[(i,currsum)] =  take # as take --> True so you can return take or True any of it you want-->
            else:
                memo[(i,currsum)] =  skip

            return memo[(i,currsum)]

        
        ans = recurse(0, 0)



        #         🔥 Time: O(2^n)

        # Because it explores ALL subsets.

        # 🔥 Space: O(n)

        # Because recursion depth = n.
        return ans





























        # # topic : recursive ++ brute force recursive solutions-->


        # total = sum(nums)

        # if (total % 2 != 0):
        #     return False

        # target = total // 2



        # def recurse(i, currsum):


        #     if (currsum == target):
        #         return True
            
        #     if (i == len(nums) or (currsum > target)):
        #         return False


        #     # option 1 : take-->
        #     take = recurse(i + 1, currsum + nums[i])

            

        #     skip = recurse(i + 1, currsum)

        #     if (take):
        #         return take # as take --> True so you can return take or True any of it you want-->
        #     else:
        #         return skip

        
        # ans = recurse(0, 0)



        # #         🔥 Time: O(2^n)

        # # Because it explores ALL subsets.

        # # 🔥 Space: O(n)

        # # Because recursion depth = n.
        # return ans






























    