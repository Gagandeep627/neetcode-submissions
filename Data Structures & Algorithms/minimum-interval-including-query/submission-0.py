class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        



        # topic : brute force solutions :

        if not intervals:
            return []

        res = []

        for q in queries:

            min_length = float("inf")    

            for (s, e) in intervals:

                if (s <= q <= e):

                    min_length = min(min_length, (e-s+1))


            if (min_length == float("inf")):
                res.append(-1)
            else:
                res.append(min_length)

        return res



