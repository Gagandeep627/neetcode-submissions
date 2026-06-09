class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        



        # topic : brute force solutions :

        if not intervals:
            return []


        # for storing the result array : O(Q)
        res = []


        # O(q) : no . of queries
        for q in queries:

            min_length = float("inf")    


            # O(n) : n : no. of intervals
            # Because for every query we scan all intervals.
            for (s, e) in intervals:

                if (s <= q <= e):

                    min_length = min(min_length, (e-s+1))


            if (min_length == float("inf")):
                res.append(-1)
            else:
                res.append(min_length)

        # Q : no. of queries
        # n : no. of intervals
        # time complexity : O(Q * n);

        return res



