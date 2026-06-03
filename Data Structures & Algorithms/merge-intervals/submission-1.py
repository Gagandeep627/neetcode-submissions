class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # topic : optimal approach (sorting + Intervals concept);
        # sort intervals based on starting time
        # O(n log(n))
        intervals.sort()


         # take first interval
        curr = intervals[0]

        # O(n)
        res = []

        #traverse remaining intervals
        # O(n)
        for i in range(1, len(intervals)):

            # if intervals overlaps
            if (intervals[i][0] <= curr[1]):
                # merge intervals
                curr[1] = max(curr[1], intervals[i][1])

            else: 

                # store current intervals
                res.append(curr)

                # move to next interval
                curr = intervals[i]

        # add last intervals
        res.append(curr)

        # answer : result;

        # total time : O(N * log(n))
        # space complexity : O(N);
        return res


        