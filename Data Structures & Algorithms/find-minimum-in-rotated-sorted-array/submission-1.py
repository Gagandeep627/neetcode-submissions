class Solution:
    def findMin(self, nums: List[int]) -> int:



        # Topic : Binary search ->
        #time_complexity : O(log n) time



        left, right = 0, len(nums) - 1
        # untill left gets == right it will run
        while (left < right):

            # mid calculated so the nums is divided int o 2 halfs and we will check 
            #each half indivisually...
            mid = (left + right) // 2


            #if suppose  middle element is > than rightest element then 
            #shorter element may have existed right side of the nums
            #so left = mid + 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                #else element could have existed in the left most side of the nums
                #so right is updated to mid - 1 to the index will be mid...
                right = mid


        
        #untill left == right means we have reached so far shortest number existed so far..
        #Time_Complexity : simple_binary search : as diviided the nums in two halfs
        #for checking the every segment to evaluate the shortest element ahead -->
        #so complexity will b e log base 2 (1) : log(n)
        return nums[left]
            












        # Brute - Force - Submission - Code -->
        return min(nums)
        