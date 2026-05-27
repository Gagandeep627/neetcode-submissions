class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result =[]


        # topic : backtracking -->

        def back(start, curr_list, curr_sum):

            if (target == curr_sum):
                result.append(curr_list.copy())
                return

            if (curr_sum > target):
                return


            for i in range(start, len(nums)):
                curr_list.append(nums[i])
                back(i, curr_list, curr_sum + nums[i])
                curr_list.pop()


        
        back(0, [], 0)

        return result



            