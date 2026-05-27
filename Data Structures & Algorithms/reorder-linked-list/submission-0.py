# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:





        #case 1: middle_element -->

        slow, fast = head, head


        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        # case 2: reverse the 2nd linked_list -->

        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp


        

        # case3:

        first, second = head, prev


        while (second):
            
            temp1, temp2 = first.next, second.next 
            first.next = second
            second.next = temp1
            first, second = temp1 , temp2


        










        
        