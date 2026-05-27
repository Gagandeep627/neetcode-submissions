import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:



        # topic Heapq -->
        # stones = [-s for s in stones]
        # heapq.heapify(stones)

        # while len(stones) > 1:
        #     first = heapq.heappop(stones)
        #     second = heapq.heappop(stones)
        #     if second > first:
        #         heapq.heappush(stones, first - second)

        # stones.append(0)
        # return abs(stones[0])


#         📊 Time Complexity (Precise + Simple)
# Operation	Cost
# Building heap	O(n)
# Each pop/push	O(log n)
# Number of operations	≤ n
# ⭐ Final Time = O(n log n)

# Build heap:     O(n)
# Smashes:         n times × O(log n)
# -----------------------------------
# Total = O(n + n log n) = O(n log n)

        

        stones = [-s for s in stones]   # make all negative
        heapq.heapify(stones)

        while len(stones) >= 2:
            f = -heapq.heappop(stones)  # largest
            s = -heapq.heappop(stones)  # second largest

            if f != s:
                leftover = f - s
                heapq.heappush(stones, -leftover)  # push NEGATIVE

        # If no stones left
        if not stones:
            return 0

        # Convert back to positive
        return -stones[0]
            