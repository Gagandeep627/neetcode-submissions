import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:



        freq = Counter(tasks)

        max_heap = []
        for count in freq.values():
            heapq.heappush(max_heap, -count)   # push negative → max heap

        time = 0
        cooldown = deque()   # (remaining_count, time_when_ready)

        while max_heap or cooldown:

            time += 1
            count = None

            # Step 1: execute one task if available
            if max_heap:
                count = -heapq.heappop(max_heap)   # convert sign
                count -= 1                         # we have used 1 instance

                if count > 0:
                    cooldown.append((count, time + n))

            # Step 2: check if some task finished cooldown
            if cooldown and cooldown[0][1] == time:
                ready_count, _ = cooldown.popleft()
                heapq.heappush(max_heap, -ready_count)

        return time

        



