class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

     # topic : 2 - pointer solutions : (optimal solutions):- 

#       Input: nums = [-1,0,1,2,-1,-4]

        nums.sort()


        n = len(nums)

        res = []



        for i in range(len(nums) - 2):
            
            l = i+1
            r = n-1

            if ((nums[i] == nums[i-1]) and (i > 0)):
                continue

            

            while (l < r):


                total = (nums[i] + nums[l] + nums[r])

                if (total < 0):
                    l += 1
                


                elif (total > 0):
                    r -= 1

                

                else: # total : 0

                    

                    res.append([nums[i],nums[l],nums[r]])

                    l = l + 1
                    r = r - 1

                    # remove duplicate entries corrosponding to l;
                    
                    while (nums[l] == nums[l-1] and (l < r)):
                        l += 1

                    while (nums[r] == nums[r+1] and (l < r)):
                        r -= 1



                    # remove duplicate entries corrosponding to r;


                   


                            # remove duplicate entries 

        return res    






                































































# Overall Flow
#   Sort Array
#       │
#       ▼
# Fix one number (i)
#       │
#       ▼
# Left = i+1
# Right = n-1
#       │
#       ▼
# Compute sum
#       │
#  ┌────┼────┐
#  │    │    │
# <0   >0   ==0
#  │    │     │
# L++  R--  Save Answer
#             │
#         L++, R--


























































        # topic : brute force solutions via set() creations:-

        # # topic : brute force solutions:-
        # # created a set()

        # # created a set() for : res;
        # res = set()
        # # Input: nums = [-1,0,1,2,-1,-4]
        # # nums = [-4,-1,-1,0,1,2]
        # # O(n log(n))
        # # sort all the elements in the nums in the ascending order


        # # sort() the nums in ascending order;
        # nums.sort()
        # # loop i in range(length of nums):
        # # O(n)
        # # O(n)

        # # loop i in range(len(nums)):-

        # # loop i in range(len(nums)):
        # # O(n)
        # for i in range(len(nums)):
        #     # loop j in range(i+1, lengh of nums):
        #     # O(n-1)


        #     # O(n-1)
        #     # loop j in range(i+1. len(nums)):
        #     # loop j in range(i+1, len(nums)):
        #     # O(n-1)
        #     for j in range(i + 1, len(nums)):
        #         # loop k in range(j + 1, length of nums):
        #         # O(n-2)
                
        #         # O(n-2) -> time_complexity -> O(n ^ (n-1) ^ (n-2)) -> O(n ^ n ^ n) -> O(n ^ 3);
        #         # loop k in range(j+1, len(nums)):


        #         # loop k in range(j+1, len(nums)):
        #         # O(n-2)
        #         for k in range(j + 1, len(nums)):

        #             # summations nums[i] and nums[j] and nums[k] == summation1
        #             # suppose if summations1 == 0
        #             # then set tmp : [nums of index (i),nums of index (j),nums of index (k)]
        #             # now this triplet will be constitute for summation equals to 0
                    
        #             # ~(1) : summations

        #             # nums(i, j, k) if it sums to 0;
        #             # set // assign : nums(index : i, index : j index : k)
        #             # if it sums to corrosponding 0
        #             # then store:


        #             # now suppose summation of nums(i, j, k) == 0 {
        #             # stire nums(i),(j), (k) in temp}
        #             if nums[i] + nums[j] + nums[k] == 0:

        #                 # store (nums(i), nums(j), nums(k)) in temp;
        #                 tmp = [nums[i], nums[j], nums[k]]
                        


        #                 # add the whole tuple(tmp) in the res : resultant;
        #                 # add the whole tuple (tmp) in the resultant array : res
                        
        #                 # add the tuple(tmp) --> resultant;
        #                 res.add(tuple(tmp))
        # # for each triplet say i in the resultant array
        # # add that triplet in the format of list in our 
        # # answer : [] and return the resultant answer list
        # # return answer
        # # time_complexity : O(n * (n-1) * (n-2)) :O(n * n * n) : O(n^3);
        # # time : O(n * (n-1) * (n-2)) : O(n ^ 3);  
        # # convert each tuple into list[]
        # # ans : && then after addition it to the resultant;
        # # return ans;

        # # for each trplet say iu in the resultant array 
        # # add each that trplet in the format of lists in our
        # # answer : [] and return the resultant answer list [];
        # return [list(i) for i in res]