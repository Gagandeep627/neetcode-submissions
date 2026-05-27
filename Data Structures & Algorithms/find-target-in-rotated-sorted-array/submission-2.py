class Solution:
    def search(self, nums: List[int], target: int) -> int:



            #question to be solved tommn by me too && better he kii jama naa tension
            #naah laee te better he kii ess question da optimal solution tu samjh leya he 
            #te better he kii code bhaven deakkh lee kall kall karr lavin te be
            # te better he ki jama na tension naa laee te bass bass --> te bass better he kii end!!!

        # left, right = 0, len(nums) - 1


        # while (left <= right):
        #     mid = (left + right) // 2


        #     if (nums[mid] == target):
        #         return mid


        #     # case 2 : if left side of array is sorted->

        #     if (nums[left] <= nums[mid]):
        #         if (nums[left] <= target < nums[mid]):
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     else:#case 3 : if left side of array is sorted->
        #         if (nums[mid] < target <= nums[right]):
        #             left = mid + 1
        #         else:
        #             right = mid - 1



        

        # return -1 

            
























            # Brute force approaxh : O(n)


            if target not in nums:
                return -1
            idx = nums.index(target)
            ans = idx


            return ans




            

        






















        # left,  right = 0, len(nums) - 1


        # while (left < right):


        #     mid = (left + right) // 2


        #     if (nums[mid] < target):
        #         left = mid + 1
        #     elif (nums[mid] == target):
        #         return mid
        #     else:
        #         right = mid


        # return -1



            


        