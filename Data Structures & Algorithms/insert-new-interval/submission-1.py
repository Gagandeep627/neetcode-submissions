class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        


        # topic : brute force solutions : 

        # add new interval into intervals array
        intervals.append(newInterval)

        # o(n * log(n))

        # sort acdn. to starting time
        intervals.sort(key = lambda x : x[0])


        # O(n)
        # store final merged intervals
        res = []

        # O(n)
        # process every intervals
        for interval in intervals:

            start = interval[0]

            end = interval[1]


            # if result is empty
            # or no overlaps exists

            if not res or (start > res[-1][1]):
                
                # directly add interval
                res.append([start, end])
            
            else:
                # overlap exists
                # merge intervals

                # update ending time
                res[-1][1] = max(res[-1][1], end)


        # time : o(n * log(n)) + O(n) : o(n * log(n))
        # space : O(n);

        # answer : result
        return res


