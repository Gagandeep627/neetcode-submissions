class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # topic : Optimal approach:- (reverse cyle methodology ++ 2-Pointer Approach Utilized):_

        n = len(nums)

        # handle cases where k > n
        k = k % n
        

        # step1 : reverse the entire nums array:
        # reverse the whole array
        # O(n)
        nums.reverse()



        # step 2: reverse the first k elements in the reversed sorted array:-
        # reverse the first k elements
        l = 0
        r = k-1
        # O(K)
        while (l < r):

            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        
        # step3 : reverse the last (n-k) (remaining elements) th elements present in afterwards
        # the k th element in the array:


        # reverse remaining elements (n-k) th elements from the array;

        l = k
        r = n-1
        # O(n-k)
        while (l < r):

            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # time : O(n) + O(K) + O(n-k) : O(n);
        # space : O(1);

        


        








































#         # topic : brute force solutions:-

#         n = len(nums)


#         k = k % len(nums)

# # For this example:

# # k = 4 % 4
# #   = 0

# # since k = 0 , no rotations is needed and the array remains:
# # [1,2,3,4]

#         k = k % n

# Outer loop: Runs k times. O(K)
#         # rotate teh array k times
#         for _ in range(k):
            
#             # stores the last element
#             l = nums[n-1]

# Inner loop: Shifts n elements each time. O(n)
#             # shift every elemnet one step to the right
#             for i in range(n-1, 0, -1):
#                 nums[i] = nums[i-1]

#             # place the last element at the beginning
#             nums[0] = l


# time : O(k * n);
# space : O(1)

        



            


        