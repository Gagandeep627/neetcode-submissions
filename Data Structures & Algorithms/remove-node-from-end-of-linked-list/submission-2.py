# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:




        # brute_force_solutions : space : O(N) -->

        # brute force solutions : 

        # assign length equals to be : 0
        # assign length equals to be : 0
        length = 0

        # assign curr pointer pointing towards head;

        # assign cur pointer pointing towards head;
        curr = head
        #O(n)


        # loop untill cur exists

        # loop untill curr exists.
        while (curr):

            # increment length val by 1 : which will provide us the total length of linked list

            # increment length (val) by 1: which will provide us teh total length of linked list
            length += 1

            # move current pointer by 1 (node)

            # move current pointer by 1 (node);
            curr = curr.next

        # now find out the psotion to remove from front
        # which will be pos_to_remove : length - n


        # now find out the position to remove from front 
        # which will be position_to_remove : length - n
        pos_to_remove = length - n



        # now suppose positon_to_remove is 0
        # then just return the next node to the (head)


        # now suppose position to be removed is 0.
        # then just return the next node to the (head)
        if (pos_to_remove == 0):
            return head.next
        

        # assign current node : (head)
        curr = head
        #O(n)


        # loop _ untill in range(0 , position_to_be_removed - 1):
        for _ in range(0, pos_to_remove - 1):
            # move current pointer by 1

            # this will reach to (node) previous to the node which is to be removed
            curr = curr.next

        # assign current.next = current (Node).next.next if suppose (current.next exists) else it will be assigned to (None);
        curr.next = curr.next.next if (curr.next) else None



        # time : O(2N) : O(N), space : O(N)
        
        return head


        
        # topic : Optimal Solutions:-


        #[[|| to be summarozed once again in Night ||]]

        # suppose if head  doesnt exists 
        # or elif (head.next doesnt exists and (removal node from end is : 1))
        # if (not head) or (not head.next and n == 1):
        #     # then our result linked list will be : Null;
        #     # return result;
        #     return None

        # # suppose N : (no. of nodes);

        # # set dummy = ListNode(0)
        # dummy = ListNode(0)
        # # set dummy.next = head
        # dummy.next = head

        # # set slow, fast both == dummy
        # # so here first of all 
        # # step : 1
        # # we have set slow , fast pointer set out to dummy;
        # slow, fast = dummy, dummy

        # # O(X(n) : no. of nodes to be reach from the last : can be uptill n : so O(n))
        # # now move fast -> fast.next untill loop till range O(N):-
        # # loop untill the range of (n):
        # # step 2:-
        # # and move fast pointer 1 step forward-
        # for _ in range(n):
        #     fast = fast.next

        # # O(n); --> time_complexity --> O(N : no. of nodes)
        # # --> O(N : no. of nodes);
        # # now untill (fast.next) exists:->
        # # step 3:-
        # # loop untill fast.next exists:-
        # # and move slow pointer 1 step ahead
        # # and move fast pointer 1 step ahead
        # while (fast.next):
        #     # move slow ahead by 1 unit
        #     slow = slow.next
        #     # move fast ahead by 1 unit
        #     fast = fast.next

        # # connect slow pointer with the slow.next.next pointer..
        # # after step 3 : connect slow with slow.next.next pointer
        # slow.next = slow.next.next

        # # ans : dummy.next
        # # return ans;
        # # ans : dummy.next
        # # return ans;
        # return dummy.next


        # #### || end ||




        # # optimal solution : space : O(1) && time : O(n)
        # # if (not head) or (not head.next and n == 1):
        # #     return None

        # # dummy = ListNode(0)
        # # dummy.next = head

        # # slow, fast = dummy, dummy
        # # for _ in range(n):
        # #     fast = fast.next


        
        # # while (fast.next):
        # #     slow = slow.next
        # #     fast = fast.next

        
        # # slow.next = slow.next.next


        # # return dummy.next




        


        






        
        


























        

        # brute_force_solutions : space : O(N) -->

        # brute force solutions -->



        length = 0 # length : 0

        # set current : head*
        curr = head
        #O(n)

        # while curr exists :
        # increment current by 1 node next()
        # O(n)
        while (curr):
            length += 1
            curr = curr.next

        # position to remove (from front) : is : (length - position of node to be removed from the end). 
        pos_to_remove = length - n


        # if the position to remove (from front)
        # is indexed : 0
        # ans =  head.next linked list , return the all other linked list except the first
        # node
        if (pos_to_remove == 0):
            return head.next
        


        # set current pointer : header*
        curr = head
        #O(n)


        # loop _ in range(0 : the index, pos_to_remove-1):
        # pos_to_remove : position to remove the node 
        # pos_to_remove - 1 : we will reach 1 position previous to the node* which needs to be removed from the
        # linked_list that : (node)*

        # O(n) : worst case position to be removed can be 1 st from the end;
        for _ in range(0, pos_to_remove - 1):
            # move 1 by 1 node ahead;
            curr = curr.next

        # remove that next node which needs to be removed next to the previous node*
        # assign the next of the current node with the current.next.next (node)*
        # if suppose next nodetro the current exists only then else
        # assign next node of the current node* to be None;
        curr.next = curr.next.next if (curr.next) else None


        # time : O(n) + O(n) : O(2*N) : o(N)
        # time : O(2N) : O(N), 

        # space : O(1);


        # answer : header*
        # return answer;
        return head




