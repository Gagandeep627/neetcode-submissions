"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
      


        # topic : brute force solutions:-


        rooms = []
        # placed = None

        intervals.sort(key = lambda x : x.start)



        for interval in intervals:
            
            start = interval.start

            end = interval.end

            placed = False

            for i in range(len(rooms)): 

                if (start >= rooms[i]):

                    rooms[i] = end
                    placed = True
                    break

            
            if not placed:
                rooms.append(end)

        ans = len(rooms)

        return ans
        