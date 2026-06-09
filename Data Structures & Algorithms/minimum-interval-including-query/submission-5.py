class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        



        # topic : Optimal Solutions :-

        # n : length of intervals
        # O(n log(n))

        # sort intervals by starting point
        # this helps to process intervals from left - right
        intervals.sort()


        # q : length of queries
        # O(q*log(q))

        # Store each query along with its original index.
        # We need the original index because after sorting
        # the queries we must put answers back in the correct position.
        sorted_queries = sorted(
            [(q,i) for(i, q) in enumerate(queries)]
        )

        # O(n) for heap

        # Min Heap
        # Stores:
        # (interval_length, interval_end)
        #
        # Smallest interval length will always stay at the top.
        heap = []


        # final answer array:
        ans = [-1] * len(queries)

         # Pointer used to traverse intervals.
        i = 0

        # process every query 1 by 1
        for q, idx in sorted_queries:

            # no. of operations been doen till it : (n (intervals) + q (queries))
            # add interval in the heap untill start of interval is < sorted_query[index]:--
            

            # add all intervals whose start <= current query
            # these intervals are now eligible to contain
            # the current query or future queries --> (A)
            
            
            while (i < len(intervals)) and (intervals[i][0] <= q):
                # (A)
                # now both intervals and queries array are sorted on the basis of the start index.
                # so suppose if query for a particular interval is being processed valid requirement
                # via its (start) < query: -- (x)
                # add that interval in the our heap
                # and move pointer i by 1 
                # now the next interval will be checked for that query again on  meeting again
                # on checking requirements // conditions of (x) are meeting or not
                # and if statemnet computes to false then i will remain as it is
                # and (next) : (query, index) will be checked from the sorted_queries
                # and will be matched for requirements with the current_index : i for intervals[index : i]
                # now as queries are also sorted so the next query will be larger than previous 
                # query and may or may not fit to the the previous interval
                # but the current and next interval will be providing the highest start interval than previous interval
                # in order to fit for that interval : and once that point has been breached 
                # after sorting multilple checks arent required for checking conditions of 
                # query with the intervals(start) : once is ocndition falsed then its the highest form uptill
                # the condition is being satisfied and after that no particular checks
                # and to the prevuious checks are not required as either they may have the start interval
                # quites less than current_interval reaching start <= query so as to give 
                # query a minimum interval index; 

                # so this was all about the logic for this problem , now try, solve and resolve the next problems over the coming queue;

                s = intervals[i][0]
                e = intervals[i][1]

                # evaluate interval length
                lenth = (e-s+1)
                # heap operations : 
                # O((n + q) * log(n));

                # push into heap
                heapq.heappush(heap, (lenth, intervals[i][1]))

                i += 1


            # check if the heap[0][1] (with minimum right_end is < query):
            # remove that query the initial minimum query from the heap 
            # stored initially
            
            # remove intervals that can no longer contain
            # the current query
            # if the interval_end < query:
            # then that interval is useless now.
            while ((heap) and (heap[0][1] < q)):
                heapq.heappop(heap)

            # if heap is not empty, 
            # top element contains the shortest valid interval.
            # else : 
            # assign ans[index] = heap[0][0] : length wkill be stored at 0 th index only:
            if heap:
                ans[idx] = heap[0][0]


    # result = answer

    # return answers in original query order.
        res = ans


         #time complexity : O((n + q) * log(n));
        #  space complexity : O(n);

        return res




# Interview-Level Explanation

# Since both intervals and queries are sorted, the interval pointer i never needs to be reset. Each interval
#  is added to the heap exactly once when its start becomes less than or equal to the current query. The heap stores (interval_length, right_end) and
#   always keeps the shortest valid interval at the top. After removing expired intervals, heap[0][0] directly gives the length of the smallest interval
#    containing the current query. This is why the solution runs efficiently without reprocessing intervals. ✅






        



