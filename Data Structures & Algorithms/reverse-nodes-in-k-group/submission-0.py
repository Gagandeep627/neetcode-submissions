# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        # topic : brute force -->
        curr = head
        values = []

        # O(n)
        while (curr):
            values.append(curr.val)
            curr = curr.next

        
        # O(m <= n as per % k iterations with len(values)) -->
        for i in range(0, len(values), k):
            if (i + k <= len(values)):
                values[i : i + k] = values[i : i + k][::-1]


        
        # O(n) --> list nodes values -->
        dummy = ListNode(0)
        curr = dummy

        for val in values:
            curr.next = ListNode(val)
            curr = curr.next

        
        # time : O(n) , space : O(n)
        return dummy.next

        






