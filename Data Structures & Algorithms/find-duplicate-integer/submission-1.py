class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        #Topic : Floyd’s Tortoise and Hare Algorithm (Cycle Detection)
        # space : O(1) : Optimal solutions to resolve the problemns.. ++ : ++ ??
        slow = 0
        fast = 0


        # step1 : frst find out with the intersection point 
        # where slow and fast meet -->
        while (True):
            slow = nums[slow]
            fast = nums[nums[fast]]

            if (slow == fast):
                break

        slow = 0

        # after the fast pointer where cycle too exists then set slow --> 0
        # then move slow and fast pointers untill they usually catch 
        # each other and once they catch --> just break the while loop -->
        # and then return the slow pointer which will depict the --> number 
        #which is repeating frequent in the nums where possibly cycle do eixsts
        while (slow != fast):

            slow = nums[slow]
            fast = nums[fast]



    # Time : O(n) , space : O(1)
        return slow



        