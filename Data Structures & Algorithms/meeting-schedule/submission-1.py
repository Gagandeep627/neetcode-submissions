"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:



        # topic : brute force solutions:-

        # O(n)
         # Outer loop:
        # Pick one meeting at a time as the current meeting.
        for i in range(len(intervals)):
            # O(n)
            # Inner loop:
            # Compare the current meeting with all meetings
            # that come after it.
            for j in range(i+1, len(intervals)):
                    # O(1)
                     # Extract start and end times
                # of the first meeting.
                    s1, e1 = intervals[i].start, intervals[i].end
                    # O(1)
                    s2, e2 = intervals[j].start, intervals[j].end

                    # check whether the two meeting overlaps
                    # overlap exists then :
                # start1 < end2 and satrt2 < end1
                # therefore overlap exists.
                    if ((s1 < e2) and (s2 < e1)):

                        # conflict found
                        # prerson cannot attend all meetings.
                        return False

        # time : O( n * n) : O(n ^ 2);
        # space : O(1)

        # all meetings pairs checked.
        # no overlap found
        return True
        



