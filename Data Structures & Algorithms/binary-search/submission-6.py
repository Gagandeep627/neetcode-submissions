class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        # topic : brute force:-
        ans = -1
        if target not in nums:
            return ans

        idx = nums.index(target)
        #[ ans : index : idx]
        return idx




















        # #Method : Binary_Search -->
        # # Time_Complexity : O(log(N))

        # left = 0
        # right = (len(nums) - 1)

        # if (len(nums) == 0):
        #     return -1



        # while (left <= right):

        #     mid = (left + right) // 2

        #     if (nums[mid] == target):
        #         return mid

        #     elif nums[mid] > target:
        #         right = mid - 1
            
        #     else:
        #         left = mid + 1


        # return -1


        







