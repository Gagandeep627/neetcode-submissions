# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        

        # topic : brute force solutions -->


        def dfs(node):
            # if not any node existed height --> so return  height : 0 there...
            if not node:
                return 0


            
            left_h = dfs(node.left)
            # if at left_h condn false immediatly ans -> False
            if (left_h == -1):
                return -1

            right_h = dfs(node.right)
            # if at right_h condn false immediatly ans -> False
            if (right_h == -1):
                return -1
            # check for tree balanced condition  
            if abs(left_h - right_h) > 1:
                return -1

            
            # return maximum height to a node in a trees-->
            return 1 + max(left_h, right_h)



        # time : O(n : no. of nodes in a trees)
        # space : O(H : height of the tree can be O(n) if a skewed tree && o(log(n)
        #  if a balanaced tree so it is considered as the O(log(n)) so thats why taking with the
        # average case comparisions uptill the O(H : Height of the tree version)
        return dfs(root) != -1
        