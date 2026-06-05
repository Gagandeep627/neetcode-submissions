"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
      


        # topic : optimal solutions -- (min heap):-

        # no meetings
        if not intervals:
            return 0
        # O(n) : all meetings overlap, all end times stored in the heap.
        
        # stores endig time of meetings : min-heap
        heap = []


        #time : o(n ^ log(n))

        # sort meetimngs accdn. to the start time.
        intervals.sort(key=lambda x : x.start)
        
        #time : O(log(n))
        # first meetings always needs one room
        heapq.heappush(heap, intervals[0].end)


        # process remaining meetings
        for i in range(1, len(intervals)):
# current meeting start time
            startl = intervals[i].start
# current meeting end time
            endl = intervals[i].end

# room becomes free
# curr_meeting can reuse that room
            if (startl >= heap[0]):

                # remove earliest ending meeting
                #time : O(log(n))
                heapq.heappop(heap)



            # push current meeting ending time.
            # either reused room or new room
            heapq.heappush(heap, endl)

        # time : O(n * log(n)) + log(n) : O(n * log(n))
        # heap size : no. of rooms used.
        ans = len(heap)



#         👉 Heap top always tells:

# which room becomes free first

# So we never waste time checking all rooms manually.
        return ans



        

        
        