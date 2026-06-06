class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        


        # topic : brute force solutions : 


        intervals.append(newInterval)


        intervals.sort(key = lambda x : x[0])

        res = []


        for interval in intervals:

            start = interval[0]

            end = interval[1]


            if not res or (start > res[-1][1]):

                res.append([start, end])
            
            else:

                res[-1][1] = max(res[-1][1], end)


        
        return res


