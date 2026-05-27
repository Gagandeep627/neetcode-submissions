class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets, result = [], []


        def backtrack(idx):

            # when idx --> len(nums) -> add the result to the subsets -->
            if ((idx) == len(nums)):
                result.append(subsets[:])
                return

            # exclude --> nums[idx]
            backtrack(idx + 1)
            
            # include -->  nums[idx]
            subsets.append(nums[idx])
            backtrack(idx + 1)
            subsets.pop()# undo the choices -->


#         Complexity

# Time: O(2ⁿ) — each element has 2 choices (include/exclude)

# Space: O(n) for recursion stack (plus result storage)
        # Recurse for Index : 0..
        backtrack(0)
        


        return result

        