# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 and not l2:
            return None

        num1 = 0
        curr = l1
        place = 1

        while (curr):
            num1 += curr.val * place
            curr = curr.next
            place *= 10


        num2 = 0
        curr = l2
        place = 1

        while (curr):
            num2 += curr.val * place
            curr = curr.next
            place *= 10



        
        total = num1 + num2

        dummy = ListNode(0)
        curr = dummy

        while (total > 0):
            digit = total % 10
            curr.next = ListNode(digit)
            curr = curr.next
            total = total // 10


        


        return dummy.next if dummy.next else dummy
