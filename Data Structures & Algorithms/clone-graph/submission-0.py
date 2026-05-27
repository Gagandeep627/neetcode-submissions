"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = 0
        self.neighbors = neighbors if neighbors != None else []   


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        visited = {}

        def dfs(curr):

            # base case 1 :
            if curr in visited:
                return visited[curr]

            clone = Node(curr.val)
            visited[curr] = clone


            for neigh in curr.neighbors:
                clone.neighbors.append(dfs(neigh))

            return clone


        return dfs(node)
