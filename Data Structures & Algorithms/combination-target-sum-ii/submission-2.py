class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        


        # sort the candidates...
        candidates.sort()
        # result array...
        result = []


        def backtrack(start, curr_list, curr_sum):

            

            # base case 1:
            if (curr_sum == target):
                result.append(curr_list[:])
                return

            # base case 2:
            if (curr_sum > target):
                return
            # start will set to 0 and start depicting to the main function
            #  after i will reach length every time
            # then start will change from 0 --> start intial value to start + 1 uptill it reaches 
            # last 2 nd most index to the candidates
            # i will move from start --> len(candidates))-->
            for i in range(start, len(candidates)):
                # condition to check i is in the diff level so that no
                # same elements are compared then compare it with the (cand[i-1] && cand[i])
                # if (true): continue..
                if (i > start and candidates[i] == candidates[i-1]):
                    continue

                # add cand[i] --> cur_list
                curr_list.append(candidates[i])
                # recurse(change i, change curr_list,change curr_sum)
                backtrack(i + 1, curr_list, curr_sum + candidates[i])
                # remove element from the last after
                # checking for addition after additon 
                # remove element one by one from end and check for other elements of present in the candidates
                # existed so far..
                curr_list.pop()


        # backtrack function (start : 0 , curr_list : []., curr_sum : 0)
        backtrack(0, [], 0)

        # Time Complexity : O(n * 2^n)

# Why?

# each element has 2 choices → include or exclude
# → so worst case = 2^n subsets checked

# and we do O(n) extra cost sometimes for copying / exploring combinations

# So final complexity: O(n * 2^n)
# Space Complexity = O(n) (recursion + current combination)

        return result
        