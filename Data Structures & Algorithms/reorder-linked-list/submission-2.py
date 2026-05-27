# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:







        # topic : space : O(N) :

        nodes = []
        curr = head

        while (curr):
            nodes.append(curr)
            curr = curr.next

        

        left, right = 0, len(nodes) - 1

        while (left < right):
            nodes[left].next = nodes[right]
            left += 1


            if (left == right):
                break


            nodes[right].next = nodes[left]
            right -= 1

        nodes[left].next = None



        


        # return head














        # topic : O(1) : space -->

        #case 1: Finding the middle element of the linked_list -->

    #     slow, fast = head, head

    # # O(n)
    #     while (fast and fast.next):
    #         slow = slow.next
    #         fast = fast.next.next

    #     prev = None
    #     curr = slow.next
    #     slow.next = None
    #     # case 2: reverse the second half of the linked_list -->
    #     # O(n)
    #     while (curr):
    #         temp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = temp


        

    #     # case3:Merger the 2 Halves of the linked list -->
    #     # O(n)
    #     first, second = head, prev


    #     while (second):

    #         temp1, temp2 = first.next, second.next
    #         first.next = second
    #         second.next = temp1
    #         first , second = temp1, temp2



        
        # time complexity : O(N). ++ : ++ ??            











            
            # temp1, temp2 = first.next, second.next 
            # first.next = second
            # second.next = temp1
            # first, second = temp1 , temp2


        










        
        