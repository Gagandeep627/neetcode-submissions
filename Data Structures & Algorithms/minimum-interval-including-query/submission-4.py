class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        



        # topic : Optimal Solutions :-

        # n : length of intervals
        # O(n log(n))

        
        intervals.sort()


        # q : length of queries
        # O(q*log(q))
        sorted_queries = sorted(
            [(q,i) for(i, q) in enumerate(queries)]
        )

        # O(n) for heap
        heap = []

        ans = [-1] * len(queries)

        i = 0


        for q, idx in sorted_queries:

            # no. of operations been doen till it : (n (intervals) + q (queries))
            # add interval in the heap untill start of interval is < sorted_query[index]:--
            while (i < len(intervals)) and (intervals[i][0] <= q):

                s = intervals[i][0]
                e = intervals[i][1]


                lenth = (e-s+1)
                # heap operations : 
                # O((n + q) * log(n));
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


         #time complexity : O((n + q) * log(n));
        #  space complexity : O(n);

        return res




# Interview-Level Explanation

# Since both intervals and queries are sorted, the interval pointer i never needs to be reset. Each interval
#  is added to the heap exactly once when its start becomes less than or equal to the current query. The heap stores (interval_length, right_end) and
#   always keeps the shortest valid interval at the top. After removing expired intervals, heap[0][0] directly gives the length of the smallest interval
#    containing the current query. This is why the solution runs efficiently without reprocessing intervals. ✅






        



