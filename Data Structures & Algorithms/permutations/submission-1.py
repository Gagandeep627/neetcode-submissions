class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        result = []
        visited = [False] * len(nums)

        def backtrack(path):

            # topic : backtracking.. : //


            # base case length of path gets equal to length of nums-->
            if (len(path) == len(nums)):
                result.append(path[:])
                return
            # first from start :--> i will run to len(nums)
            # 
            for i in range(0, len(nums)):
                # if that i is not visited-->
                if not visited[i]:
                    # add(nums[i]) to path-->
                    path.append(nums[i])
                    # set visited[i]--> true
                    visited[i] = True

                    # backtrack go deeper
                    backtrack(path)
                    # undo the path and try again for other possible options for 
                    # path ->
                    path.pop()
                    # set visited[i]== False;
                    visited[i] = False

        # set initial path : ([])

        # Time Complexity = O(n × n!) : Generating n! permutations, copying each of length n
        # → So total auxiliary space = O(n) : Recursion depth + path + used array
        backtrack([])
            

        return result

            
        