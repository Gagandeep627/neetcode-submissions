import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # topic : heapq/ priority queue -->
        # O(m)

        # take a freq counter-->
        freq = Counter(tasks) # O(1)

        max_heap = []

        #  O(26 log 26)  → O(1)
        # store all the -count in the heap
        # so as to create a max_heap-->
        for count in freq.values():
            heapq.heappush(max_heap, -count) # O(1)   # push negative → max heap

        # set : time : 0
        time = 0
        cooldown = deque() # cooldown as a deque(storing remaing_count, time_when_ready)-->   # (remaining_count, time_when_ready)
        # m + idle cycles : Worst-case idle cycles also proportional to m (because cooldown forces spacing).
        while max_heap or cooldown: #untill max_heap or 
            #cooldown deque --> exists --> inc(time) , set(count) --> None

            time += 1
            count = None

            # Step 1: execute one task if available
            if max_heap: #length : max_heap > 1:
                # For each time step:

            # At most one heap pop → O(log 26) → O(1)
                #take the latest remaing_count from heap the maximum 
                # the maximum possible so far to use the maximum frequent
                # remaining count so far.. for heap[ to evaluate the most possible occurances for the
                # remaining count--> 
                count = -heapq.heappop(max_heap)
                #   used one instance of the frequency so decrement the count(-1) -->
                count -= 1                         # we have used 1 instance

                # if (count > 0): 
                # add(reamianing_count, time + n(cooldown peroid for each scheduling task ocurrant)
                # in our created deque for cooldown())-->
                if count > 0:
                    cooldown.append((count, time + n)) #O(1)

            # step 2: if (cooldown exists) and (cooldown[0][1] (remaining time left for the cool
            # cooldown the required scheduled tasks --> if matches to the time))->
            if cooldown and cooldown[0][1] == time:
                # remove it --> take the remaining count for the 
                # scheduled tasks whopes cooldown time has been elapsed
                ready_count, _ = cooldown.popleft()
                # At most one heap push → O(log 26) → O(1)
                # add (ready_count) to the max_heap -ve sign : for addition in the
                # max_heap-->
                heapq.heappush(max_heap, -ready_count)



        # Final Time Complexity : O(m);
        # Final Space Complexity : O(1);
        return time # ans : time;

        



