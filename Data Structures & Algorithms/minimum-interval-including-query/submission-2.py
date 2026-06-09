class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        



        # topic : brute force solutions :

        if not intervals:
            return []


        # for storing the result array : O(Q)

        # Store answers for all queries
        res = []


        # O(q) : no . of queries

        # pick 1 query at a time:
        for q in queries:

            min_length = float("inf")    


            # O(n) : n : no. of intervals
            # Because for every query we scan all intervals.

            # assume no valid interval
            for (s, e) in intervals:
                

                # check whether query lies inside the interval
                if (s <= q <= e):
                    # evaulate the interval length
                    min_length = min(min_length, (e-s+1))

            # if no interval contained the query
            if (min_length == float("inf")):
                res.append(-1)

            # otherwise store the shortest interval length
            else:
                res.append(min_length)

        # Q : no. of queries
        # n : no. of intervals
        # time complexity : O(Q * n);
        # space : O(Q);
        # return answers of all queries;

        # return result;
        return res



