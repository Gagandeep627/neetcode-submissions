# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        



        # brute_force_solutions : space : O(N) -->


        length = 0


        curr = head
        #O(n)
        while (curr):
            length += 1
            curr = curr.next


        pos_to_remove = length - n

        if (pos_to_remove == 0):
            return head.next
        
        curr = head
        #O(n)
        for _ in range(0, pos_to_remove - 1):
            curr = curr.next

        
        curr.next = curr.next.next if (curr.next) else None



        # time : O(2N) : O(N), space : O(N)
        return head




