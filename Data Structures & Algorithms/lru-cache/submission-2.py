class Node:
    def __init__(self, key, val):

        # intialize for the instance key, val
        self.key = key
        self.val = val
        # and intializing instance for prev, next
        self.prev = None
        self.next = None


class LRUCache:

    # Topic : Doubly Linked_List and hash_Map_(Python : dictionary concept)..//..

    def __init__(self, capacity: int):

        # intiallize cap to capacity:
        self.cap = capacity
        # create a cache dictionary():-
        self.cache = {}  # key -> Node
        # Create dummy head and tail to simplify operations
        
        # set a left , right pointer to Node(0,0)
        # right pointer : Node(0,0)
        self.left, self.right = Node(0, 0), Node(0, 0)
        # assign next pointer of left to right 
        # assign previous pointer of right pointer to left
        self.left.next, self.right.prev = self.right, self.left


    # Helper function: remove a node
    # helper function: to remove a node
    def remove(self, node):
        # set prev pointer to node.prev
        # and nxt pointer to node.next pointer
        prev, nxt = node.prev, node.next
        # set prev.next pointer to nxt
        # assign nxt.prev pointer to prev
        prev.next, nxt.prev = nxt, prev

    
    # Helper function: insert node at the right (MRU end)
    # helper function : insert node at the right (MRU end)
    def insert(self, node):
        
        # set prev pointer to 
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt


    def get(self, key: int) -> int:

        if key in self.cache:
            # Move the accessed node to the MRU end
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            # Remove old node to update its position
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])


        if len(self.cache) > self.cap:
            # Remove from LRU end (left side)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


    #Average time complexity : O(1) && Average space complexity : O(1)

        
