"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:



        # topic : Optimal approach solutions:-

        
        intervals.sort(key = lambda x : x.start)

        # prev = intervals[0]

        for inte in range(1, len(intervals)):
            
            prev = intervals[inte-1]
            curr = intervals[inte]


            # if current start < previous end : conflict arises-

            if (curr.start < prev.end):
                return False


        return True




