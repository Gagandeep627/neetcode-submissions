class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        



        candidates.sort()
        result = []


        def backtrack(start, curr_list, curr_sum):

            


            if (curr_sum == target):
                result.append(curr_list[:])
                return

            
            if (curr_sum > target):
                return




            for i in range(start, len(candidates)):

                if (i > start and candidates[i] == candidates[i-1]):
                    continue



                curr_list.append(candidates[i])
                backtrack(i + 1, curr_list, curr_sum + candidates[i])

                curr_list.pop()


            
        backtrack(0, [], 0)

        return result
        