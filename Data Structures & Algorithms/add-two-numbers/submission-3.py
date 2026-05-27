# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        



        # Time : O(n + m) , Space : O(1)...
        if not l1 and not l2:
            return None

        num1 = 0
        curr = l1
        place = 1
        # convert l1 into number -->
        while (curr):
            num1 += curr.val * place
            curr = curr.next
            place *= 10

        num2 = 0
        curr = l2
        place = 1
# convert l2 into number -->
        while (curr):
            num2 += curr.val * place
            curr = curr.next
            place *= 10
# then make the total
        total = num1 + num2

        dummy = ListNode(0)
        curr = dummy

        if (total == 0):
            return dummy
# then procdess the total to form digit one by one in reverse order
# to process to the newly formed linked list && changing total for next possible 
# digit concatation so far...
        while (total > 0):
            digit = total % 10
            curr.next = ListNode(digit)
            curr = curr.next
            total = total // 10


        return dummy.next