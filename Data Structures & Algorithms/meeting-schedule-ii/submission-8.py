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


        if not intervals:
            return 0

        heap = []

        intervals.sort(key=lambda x : x.start)

        heapq.heappush(heap, intervals[0].end)



        for i in range(1, len(intervals)):

            startl = intervals[i].start

            endl = intervals[i].end


            if (startl >= heap[0]):
                
                heapq.heappop(heap)


            heapq.heappush(heap, endl)


        ans = len(heap)

        return ans



        

        
        