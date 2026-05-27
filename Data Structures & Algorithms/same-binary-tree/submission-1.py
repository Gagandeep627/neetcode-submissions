# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        


        # topic : brute force solution
        def dfs(p, q):

            if (not p and not q):
                return True


            # to check if symmetry of the tree is different at any point any node
            if (not p and q) or (not q and p):
                return False

            
            if (p.val != q.val):
                return False


            return (dfs(p.left, q.left) and dfs(p.right, q.right))




    

        # time : O(n), space : O(h : O(log(n)) --> for balanced trees , O(n) for skewed trees) -->
        ans = dfs(p, q)
        return ans    