class Solution:
    def findDuplicate(self, nums: List[int]) -> int:





        # topic : brute force solutions -->


        mappings = {}

        # time : O(n) : n : len(nums) , space : O(n)
        for num in nums:

            mappings[num] = mappings.get(num, 0) + 1

            if (mappings[num] > 1):
                return num

            










































        #Topic : Floyd’s Tortoise and Hare Algorithm (Cycle Detection)
        # space : O(1) : Optimal solutions to resolve the problemns.. ++ : ++ ??
    #     slow = 0
    #     fast = 0


    #     # step1 : frst find out with the intersection point 
    #     # where slow and fast meet -->
    #     while (True):
    #         slow = nums[slow]
    #         fast = nums[nums[fast]]

    #         if (slow == fast):
    #             break

    #     slow = 0

    #     # after the fast pointer where cycle too exists then set slow --> 0
    #     # then move slow and fast pointers untill they usually catch 
    #     # each other and once they catch --> just break the while loop -->
    #     # and then return the slow pointer which will depict the --> number 
    #     #which is repeating frequent in the nums where possibly cycle do eixsts
    #     while (slow != fast):

    #         slow = nums[slow]
    #         fast = nums[fast]



    # # Time : O(n) , space : O(1)
    #     return slow



#         💡 Key Idea — Floyd’s Tortoise and Hare Algorithm (Cycle Detection)

# Here’s the intuitive logic 👇

# Imagine the array as a linked list:

# Each value nums[i] tells you the next index to go to.

# For example, if nums = [1, 3, 4, 2, 2],
# you can think of it as:

# 0 → 1 → 3 → 2 → 4
#           ↑     ↓
#           ←←←←←←


# The duplicate value creates a cycle in this “list”.

# Now we can apply the Floyd’s Cycle Detection algorithm, which uses:

# A slow pointer (moves one step at a time)

# A fast pointer (moves two steps at a time)

# If there’s a cycle, both pointers will eventually meet.

# Once they meet, we reset one pointer to the start and move both one step at a time until they meet again — that point will be the duplicate number.



        