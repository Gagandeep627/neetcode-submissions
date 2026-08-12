"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # Topic : Brute force via Hash_Map approach (Deep_Copy_Approach --> ) -->


        # topic : brute force via hash_map approach (deep_copy_approach) -->

        # topic : brute force via hash_map approach
        # (Deep copy research) -->


        # now suppose if head doesnt exists:
        # result is None;


        # now suppose if head doesnt exists.
        if not head:
            # return answer will be header is : (None);
            # answer : None
            return None

        # step 1 : 
        # create a map old_to_new_node= {}


        # step 1:
        # create a map old to new node : {}
        old_to_new_node = {}

        # step 1 : mappings of all the copying the node and their .next and .random pointers
        # to a hash_map -->


        # step 1 : mapping of all the copying the node and their .next and .random pointers to a hash_map -->


        # assign current node * = head*
        curr = head



        
        # loop untill (current node exists) :
        while (curr):
            # now suppose untill current node exists: create a new Node(curr.val)


            # now suppose untill current node exists: create a new Node (curr.val);
        
            # copy pointer will create
            # copy pointer will create
            # copy = Node(curr.val) 
            copy = Node(curr.val)
            # now set the current node in the map and assign its theat key pair value to :copy (Node)

            # now set the current node in the map and assign 
            # its threat key : pair value to : copy (Node)
            old_to_new_node[curr] = copy
            
            # link copy.next pointer with the curr.next
            
             
            copy.next = curr.next
            # link copy.random pointer with the current random
            copy.random = curr.random
            # move current pointer by 1 node
            curr = curr.next


        


        # step : 2 : then retrieve one by one the copied right from the head to all depicting via current
        # to .next && .random pointers Nodes one by one && return the final Head from the Linked_List -->
        #at the end return old_to_new_node[head of the Linked_List --> ]


        # assign current pointer to the head
        curr = head
        # loop untill current node exists
        while (curr):

            # assign copy pointer to the first node from the mapping of the old_to_new_node[current node]
            copy = old_to_new_node[curr]
            # link cop.next pointer with the old_to_new_node(map).get(current(node).next  pointer)
            copy.next = old_to_new_node.get(curr.next)
            #link copy.random pointer with the  old_to_new_node (map).get(curr.random)
            copy.random = old_to_new_node.get(curr.random)
            # move current pointer by 1;
            curr = curr.next

        # return the key : header node from the mappings of the
        # old_to_new_node (mapping) 
        return old_to_new_node[head]

        






        