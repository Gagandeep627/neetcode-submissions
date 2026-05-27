class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:



        # sort the nums-->
        nums.sort()
        # resultant array-->
        result = []


        def backtrack(start, path):
            
            # topic : backtracking...

            # add the current path to the result-->
            result.append(path[:])
            # base case :return : if len(path) == len(nums) -->
            if (len(path) == len(nums)):
                return

            # loop i from range(start --> len(nums)) start will be from 0 th , 1 th , 2 nd-->
            # with which i will range from (start --> nums in each iteration for backrack(start))
            for i in range(start, len(nums)):
                
                # check if i and start at not same level && nums[i] != nums[i-1] -->
                if ((i > start) and (nums[i] == nums[i-1])):
                    continue

                # add nums[i] --> path
                path.append(nums[i])
                # go deeper for backtrack for (i + 1 th route keeping start to same untill (i + 1) reaches to len(nums))
                backtrack(i + 1, path)

                # undo path && try for the unexplored nums[i] backtrack to the intial 
                # space and try with different nums[i] not visited right now..
                path.pop()


        # backtrack_functions() --> start : 0, path : []
        backtrack(0, [])
        return result



        