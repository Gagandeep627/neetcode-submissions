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

        # O(n log n) (sorting)
        # Sort all meetings according to start time.
        intervals.sort(key = lambda x : x.start)

        # prev = intervals[0]
        # O(n)
         # Traverse from second meeting onward.
        for inte in range(1, len(intervals)):
            # O(1)

             # End time of previous meeting.
            prev = intervals[inte-1]
            # O(1)

            # Start time of current meeting.
            curr = intervals[inte]


            # if current start < previous end : conflict arises-
            # Check overlap.
            # If current meeting starts before
            # previous meeting finishes,
            # a conflict exists.
            if (curr.start < prev.end):
                return False

# time : O(nlog(n)) + O(n) : O(n log(n))
# space : O(1)


# No conflicts found.
        return True




