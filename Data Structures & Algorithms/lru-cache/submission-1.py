class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    # Topic : Doubly Linked_List and hash_Map_(Python : dictionary concept)..//..

    def __init__(self, capacity: int):


        self.cap = capacity
        self.cache = {}# key -> Node
        # Create dummy head and tail to simplify operations


        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left


    # Helper function: remove a node
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    
    # Helper function: insert node at the right (MRU end)
    def insert(self, node):
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

        
