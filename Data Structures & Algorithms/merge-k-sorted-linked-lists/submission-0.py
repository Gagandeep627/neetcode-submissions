# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        
        if not lists:
            return None

        # topic : brute_force -->
        all_values = []

        for l in lists:
            curr = l
            while (curr):  
                all_values.append(curr.val)
                curr = curr.next


        
        all_values.sort()



        dummy = ListNode(0)
        curr = dummy



        for val in all_values:
            curr.next = ListNode(val)
            curr = curr.next


        return dummy.next    

    


        







    
        