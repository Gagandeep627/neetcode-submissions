# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        

        # Topic : Floyd's cycle detection algorithm / tortoise 
        #& Horse algorithm -->



        # Time : O(n)
        # Space : O(1)

        # topic : Optimal solutions. ||


        # set slow : head
        # sdet fast : head
        slow, fast = head, head

        # loop untill fast exists and fast.next exists:

        while fast and fast.next:
            # set by 1 unit
            # set slow : slow.next
            slow = slow.next
            # move fast by 2 unit
            # set fast : fast.next.next
            fast = fast.next.next


            # suppose (slow commutes to fast):
            
            if (slow == fast):
                return True


        return False

        # Topic : Floyd's cycle detection algorithm / tortoise 
        #& Horse algorithm -->



        # Time : O(n)
        # Space : O(1)

        # slow, fast = head, head



        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next



        #     if (slow == fast):
        #         return True


        # return False
        