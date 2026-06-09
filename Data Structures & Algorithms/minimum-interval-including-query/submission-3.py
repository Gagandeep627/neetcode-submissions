class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        



        # topic : Optimal Solutions :-


        intervals.sort()

        sorted_queries = sorted(
            [(q,i) for(i, q) in enumerate(queries)]
        )


        heap = []

        ans = [-1] * len(queries)

        i = 0


        for q, idx in sorted_queries:


            # add interval in the heap untill start of interval is < sorted_query[index]:--
            while (i < len(intervals)) and (intervals[i][0] <= q):

                s = intervals[i][0]
                e = intervals[i][1]


                lenth = (e-s+1)

                heapq.heappush(heap, (lenth, intervals[i][1]))

                i += 1


            # check if the heap[0][1] (with minimum right_end is < query):
            # remove that query the initial minimum query from the heap 
            # stored initially
            while ((heap) and (heap[0][1] < q)):
                heapq.heappop(heap)


            # else : 
            # assign ans[index] = heap[0][0] : length wkill be stored at 0 th index only:
            if heap:
                ans[idx] = heap[0][0]


    # result = answer
        res = ans

        return res






        



