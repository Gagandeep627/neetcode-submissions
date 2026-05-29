class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        # topic : dutch national flag algorithm:
        # l : position where next 0 should be placed
        l = 0
        # mid : current element being checked
        m = 0
        # r : poition where next 2 should be placed
        r = len(nums) - 1


        # O(n)
        # process array untill mid crosses high
        while (m <= r):


            # case : 1
            # if current element is 0
            
            if (nums[m] == 0):
                # O(1)
                # swap current element with the low pointer
                nums[m], nums[l] = nums[l], nums[m]
                # move low forward
                l += 1
                # move mid forward
                m += 1

            # case : 2
            # if current element is 1
            elif (nums[m] == 1):
                # O(1)
                # 1 is already in the correct middle region 
                m += 1

            # case 3:
            # if current element is 2

            else:
                # O(1)
                # swap current element  with the high pointer
                nums[r], nums[m] = nums[m], nums[r]
            # move r backward
                r -= 1
                # m += 1
                # do not move mid
                # bcz swapped element needs checking

        # time : O(n)
        # space : O(1)
        # final sorted copy array;
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