class Solution:
    def search(self, nums: List[int], target: int) -> int:



        
        #applying Topic : binary search 
        left, right = 0, len(nums) - 1

        #runns until right reaches < than left...
        while (left <= right):
            mid = (left + right) // 2

            #case 1 check if mid contains the target-->
            if (nums[mid] == target):
                return mid


            # case 2 : if left side of array is sorted->
            #supposition as rotating the array would generate sorted multiple nums of array in the new nums result : if left side of the array is sorted -->
            if (nums[left] <= nums[mid]):
                #if target falls btw left && mid index of the nums -->
                if (nums[left] <= target < nums[mid]):
                    #change right to --> mid - 1to find index of the target element...
                    right = mid - 1
                else:
                    #else change if not in the left ---> mid index then elemengt would be in the next half -->
                    #change --> left --> mid + 1 search in the second half started...
                    left = mid + 1
            else:#case 3 : if left side of array is sorted->
            #Case 3 : if target in mid --> right index of the nums
                if (nums[mid] < target <= nums[right]):
                    #change left -> mid + 1 to look in the 2nd segment of the sub_nums
                    left = mid + 1
                else:
                    #else if not presenrt in the 2 nd segment then start for look over in the the 1 st segment -> via
                    #right --> mid - 1
                    right = mid - 1



        #Time_Complexity : O(log(n))
        #Space : O(1)
        #if didnt find mid means target is not present in nums...
        return -1 

            
























            # Brute force approaxh : O(n)


            # if target not in nums:
            #     return -1
            # idx = nums.index(target)
            # ans = idx


            # return ans




            

        






















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



            


        