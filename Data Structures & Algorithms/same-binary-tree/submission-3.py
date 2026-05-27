# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        

        # topic : dfs approach (brute force):-

        # topic : brute force solution
        # function dfs(p, q);
        def dfs(p, q):
            
            # if both nodes doesnt exists corrosponding to the tree then tehy are
            # suymmetrical identical trees-->
            if (not p and not q):
                return True


            # to check if symmetry of the tree is different at any point any node
            # doesnt exits corrosponding to the node in the other trees-->
            
            # suppose one exists and other didt exists 
            # like here : p doesnt exists and q exists
            # : q doesnt exits and p exists 
            if (not p and q) or (not q and p):
                return False

            # if val of (p, q) differ then its a false same trees-->
            
            # suppose if p.val is not equal to q.val:
            # return answer : false

            if (p.val != q.val):
                return False


            # function call for p && q both left call recursively and .right()
            # call recursively..
            # function call dfs(p.left, q.left) and dfs(p.right, q.right)
            return (dfs(p.left, q.left) and dfs(p.right, q.right))




    

        # time : O(n), space : O(h : O(log(n)) --> for balanced trees , O(n) for skewed trees) -->
        ans = dfs(p, q)
        return ans    