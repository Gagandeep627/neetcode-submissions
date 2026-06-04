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

        # space : O(n)
        rooms = []
        # placed = None
        # O(n * log(n))
        intervals.sort(key = lambda x : x.start)


        # O(n) : no. of intervals in the array of intervals
        # traverse every meeting interval object 1 by 1
        for interval in intervals:
            

            # extract current meeting start time
            start = interval.start
            # extract current meeting end time
            end = interval.end

            # flag variable:
            # checks whether current meeting got placed into some room or n
            placed = False

            # O(n)--> no. of rooms will be going to : O(n)
            # iterate through every existing room
            # rooms[i] stores ending time of the currentmeeting inside that room
            for i in range(len(rooms)): 
                

                # if current meeting starts after or exactly when
                # room becomes free
                # then same room can be reused
                # no overlap or conflict occurs
                if (start >= rooms[i]):
                    

                    # update room endingtime with curr meeting end time
                    # bcz now this room becomes occupied till end
                    rooms[i] = end


                    # mark that current meeting has been placed successfully
                    placed = True


                    # stop searching more rooms
                    # bcz room alreafy found
                    break

            # if current meeting could not fit into any existing room
            # then create a completely new room
            if not placed:
                 # append ending time of current meeting
                # meaning:
                # new room now occupied till "end"
                rooms.append(end)

        # time : O(n * n) : O(n ^ 2);
        # space : O(n)

        # total rooms used
        # length of rooms array : minimum meeting rooms required
        ans = len(rooms)

        return ans
        