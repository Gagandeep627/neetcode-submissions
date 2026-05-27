class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result =[]


        # topic : backtracking -->

        def back(start, curr_list, curr_sum):
            
            # (target == curr_sum add the subset of the curr_list to the result)-->
            # return :
            if (target == curr_sum):
                result.append(curr_list.copy())
                return

            # if (curr_sum > target) : backtrack to the functions-->
            if (curr_sum > target):
                return

            #  i have to start from the start to the len(nums) not every time fro  0 th indexed
            # as start have to point out to --> that element of the curr_list which havent been used 
            # that is : the element which is yet to be used to the next element of the i t element to the
            # curr_list -->
            for i in range(start, len(nums)):
                # add nums[i] to the curr_list
                curr_list.append(nums[i])
                # add --> curr_sum + nums[i] untill either curr_sum reaches or exceeds the target -->
                back(i, curr_list, curr_sum + nums[i])
                # undo the last element from the curr_list to explore the other paths 
                # to revaluate to calculate the curr_sums for the other  paths if getting match to
                # target in order to find a another subset for the target-->
                curr_list.pop()


        # Time Complexity: O(2^(t/m)) where m is minimum element in nums.
        # Space Complexity: O(t/m) (excluding output result list)
        back(0, [], 0)

        return result



            