class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # topic : Optimal approach:- (revrerse cyle methodology):_

        n = len(nums)
        k = k % n
        

        # step1 : reverse the entire nums array:
        nums.reverse()



        # step 2: reverse the first k elements in the reversed sorted array:-

        l = 0
        r = k-1

        while (l < r):

            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        
        # step3 : reverse the last (n-k) (remaining elements) th elements present in afterwards
        # the k th element in the array:

        l = k
        r = n-1

        while (l < r):

            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        


        








































#         # topic : brute force solutions:-

#         n = len(nums)


#         k = k % len(nums)

# # For this example:

# # k = 4 % 4
# #   = 0

# # since k = 0 , no rotations is needed and the array remains:
# # [1,2,3,4]

#         k = k % n


#         # rotate teh array k times
#         for _ in range(k):
            
#             # stores the last element
#             l = nums[n-1]


#             # shift every elemnet one step to the right
#             for i in range(n-1, 0, -1):
#                 nums[i] = nums[i-1]

#             # place the last element at the beginning
#             nums[0] = l

        



            


        