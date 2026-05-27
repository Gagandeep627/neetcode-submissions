import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        # topic : heapq-->
        min_heap = []


        # 1)create a min heap with every element for
        #  minimumm element at first via pripority
        # system to the maximum element at the end..
        # 2).if (length = min_heap goes beyond > k : then 
        # then remove the element from the front (the smallest element of the min_heap)
        # until the last k elements are left in the min_heap
        # the first element will be point to the last largest element so far
        # which will be tyhe k-th k_largest element so far..
        # Move to nxt quesns, hune tu fhilhaul tu. ++ : ++ ??

        for n in nums:

            heapq.heappush(min_heap, n)

            if (len(min_heap) > k):
                heapq.heappop(min_heap)




#         | Complexity Type | Value          | Reason                                         |
# | --------------- | -------------- | ---------------------------------------------- |
# | **Time**        | **O(n log k)** | Each of n elements does heap ops costing log k |
# | **Space**       | **O(k)**       | Min-heap stores at most k numbers              |



        
        return min_heap[0]