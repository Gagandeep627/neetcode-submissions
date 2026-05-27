class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        
        # topic : recursive ++ brute force recursive solutions-->


        total = sum(nums)

        if (total % 2 != 0):
            return False

        target = total // 2



        def recurse(i, currsum):



            
            if (currsum == target):
                return True
            
            if (i == len(nums) or (currsum > target)):
                return False


            # option 1 : take-->
            take = recurse(i + 1, currsum + nums[i])

            # if (take):
            #     return True

            skip = recurse(i + 1, currsum)

            if (take):
                return True
            return skip

        
        ans = recurse(0, 0)
        return ans






























    