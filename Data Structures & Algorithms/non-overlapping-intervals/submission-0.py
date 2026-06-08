class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        



        # TOPIC : BRUTE FORCE SOLUTIONS :-

        intervals.sort()


        n = len(intervals)


        def dfs(curr, prev):
            
            
            # base case if array reached to end then nothing needs to be removed 
            # any index : return 0
            if curr >= n:
                return 0



            # remove the current element from array

            remove = 1 + dfs(curr + 1, prev)


            # nothing is defined to keep , 
            # so assign keep : inf , bcz we have to find the removal so minimum value will be computing
            # to remove value only so therefore assigning keep to infinity.

            keep = float("inf")

            # keep the curr elements in the array:
            if (prev == -1 or (intervals[curr][0] >= intervals[prev][1])):
                keep = dfs(curr + 1, curr)


            return min(remove, keep)



        ans = dfs(0, -1)

        return ans






