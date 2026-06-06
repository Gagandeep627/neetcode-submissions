class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        


        # topic : Optimal solutions (intervals) :


        if not intervals:
            return [newInterval]

        # space : O(n)
        # for result array
        # stores final answer
        res = []

        # Input: intervals = [[1,3],[4,6]]
        #  newInterval = [2,5]


        # single traversal
        # O(n)
        for inte in intervals:

            s = inte[0]

            e = inte[1]


        #    curr_interval is not before new_interval

        # case 1: 
        # curr_interval completely before new interval
        # no overlap

            if (e < newInterval[0]):
                res.append(inte)




            # case 2: 
            # curr_interval completely after new interval
            # insert the new interval first.
            # no overlap exists

            elif (s > newInterval[1]):

                res.append(newInterval)


                # curr interval now becomes newinterval
                # helps avoid inserting the old newinterval again

                newInterval = inte




            # else : new interval lies in the range of the interval[i]
            # result will be to merge the interval
            # case 3:
            # overlap exists
            else:
                
                # merge interval by expanding boundaries
                newInterval[0] = min(newInterval[0], s)

                newInterval[1] = max(newInterval[1], e)
        
        # add remaining interval
        # important for last merged / new interval
        res.append(newInterval)


        return res



