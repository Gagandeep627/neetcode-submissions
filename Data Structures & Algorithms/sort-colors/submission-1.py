class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        # topic : dutch national flag algorithm:
        l = 0
        m = 0
        r = len(nums) - 1



        while (m <= r):



            # if current element is 0
            
            if (nums[m] == 0):
                nums[m], nums[l] = nums[l], nums[m]
                l += 1
                m += 1


            # if current element is 1
            elif (nums[m] == 1):
                m += 1


            # if current element is 2

            else:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1
                # m += 1

        return nums





































        # topic : brute force approach : (bubble sort)
        # compare adjacent element :
        # if (left > right
        # swap them
        # keep doing this multiple times.


        # n = len(nums)
        # # O(n)
        # for i in range(n):
        #     # O(n)
        #     for j in range(n-i-1):

        #         if (nums[j] > nums[j+1]):
        #             nums[j], nums[j+1] = nums[j+1], nums[j]

        # # time : O(n ^ 2)
        # # space : O(1)
        # return nums