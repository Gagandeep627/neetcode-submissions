class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        



        # TOPIC : Optimal SOLUTIONS (recursive + memoizations) :-


        # sort the interval in accdn with the start 
        # no. of each and current element
        # overlap checking becomes easier
        intervals.sort()

        # n : length of interval
        n = len(intervals)
 # Memoization dictionary
        memo = {}

        # Recursive function
        # index -> current interval we are processing
        # prev -> index of previously selected interval
        def dfs(curr, prev):
            
            
            # base case if array reached to end then nothing needs to be removed 
            # any index : return 0
            # no more removals are needed.
            if curr >= n:
                return 0

        # if answer is alreday computed
        # return it from memo
            if (curr, prev) in memo:
                return memo[(curr, prev)]


            # choice : 1
            # remove curr interval
            # count 1 removal and move to next interval.
            # remove the current element from array

            remove = 1 + dfs(curr + 1, prev)


            # choice : 2
            # keep the curr interval
            # intialize with infinity bcz
            # keeping may not always be possible

            # nothing is defined to keep , 
            # so assign keep : inf , bcz we have to find the removal so minimum value will be computing
            # to remove value only so therefore assigning keep to infinity.

            keep = float("inf")

            # check if the curr interval can be kept
            # it can be kept if :
            # 1. no . previous interval exists
            # or
            # 2. curr interval does not overlap
            # with the previous selected interval


            # keep the curr elements in the array:
            # if previous element is none or current elements start is greater than equal to previous element (end) no.
            # so in that case the interval is non-overlapping no need to remove such inetrval keep such interval
            if (prev == -1 or (intervals[curr][0] >= intervals[prev][1])):
                
                # keep current interval and
                # make it the new previous interval

                keep = dfs(curr + 1, curr)

            # return minimum removals obtained
            # from the both choices

            # store min answer in memo
            memo[(curr, prev)] = min(remove, keep)

            # return stored answer to the parent recursive call
            return memo[(curr, prev)]

        # time complexity : 
        # there are at mos n choices for index
        # n choices for prev
        # states : O(n ^ 2);


        # space : O(n ^ 2)
        # memo table : O(n ^ 2)
        # recursion stack : O(n)
        


        ans = dfs(0, -1)

        return ans






