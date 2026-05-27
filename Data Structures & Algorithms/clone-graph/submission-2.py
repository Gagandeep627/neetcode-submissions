"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = 0 #set val for newly created node --> 0;
        self.neighbors = neighbors if neighbors != None else [] # set neighbors of
        # the newly created node as [] if neighbors exited so far else
        # set the newly(Node).neighbors =  None;


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # topic : brute force -- (recursive ++ DFS approach)-->

        # and --> none (if node doesnt existed)..
        if not node:
            return None
        
        # make a record for for the
        # curr_node && newly created node with
        # mapping of its neighbors-->
        visited = {}

        def dfs(curr):

            # base case 1 :
            # check for curr in visited if yes, then return value
            # to the visited[curr]-->
            if curr in visited:
                return visited[curr]

            # create a new node deep copy of the curr_node..
            clone = Node(curr.val)
            # make visited[curr(node)] --> newly created node->
            visited[curr] = clone

            # for all neighbors do existed for curr(node)_neighbors-->
            for neigh in curr.neighbors:
                # add them to the newly_created_node[neighbors] -->
                # dfs(neighbors --> existed so far)...
                clone.neighbors.append(dfs(neigh))
            
            # backtrack and return the first newly node
            # wer have created do far..
            return clone

        # call --> dfs(Node_main (node))-->

        # ⏱️ Step 5: Time and Space Complexity (precisely)
# 🔸 Time Complexity = O(V + E)

# V = number of vertices (nodes)

# E = number of edges (connections)
# We visit each node once and clone all its edges.

# 🔸 Space Complexity = O(V)

# For the visited dictionary storing clones.

# Plus recursion stack in DFS (up to O(V) deep in worst case).
        return dfs(node)
