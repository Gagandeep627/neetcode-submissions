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


        if not head:
            return None

        # step 1 : 
        old_to_new_node = {}


        curr = head

        while (curr):
            copy = Node(curr.val)
            old_to_new_node[curr] = copy
            copy.next = curr.next
            copy.random = curr.random
            curr = curr.next


        


        # step : 2
        curr = head
        while (curr):
            copy = old_to_new_node[curr]
            copy.next = old_to_new_node.get(curr.next)
            copy.random = old_to_new_node.get(curr.random)
            curr = curr.next


        return old_to_new_node[head]

        






        