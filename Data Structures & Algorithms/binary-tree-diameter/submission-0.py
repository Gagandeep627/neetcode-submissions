# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.maxdiameter = 0
        # topic : brute force solution O(N) time -->

        
        def dfs(root):
            # if root isnt existed means --> height to that particukar node existed == 0;
            if not root:
                return 0

            # evaluate left_height for trees-->
            left_height = dfs(root.left)

            # evaluate right_height for trees-->
            right_height = dfs(root.right)
            # to calculate max_diameter as per the formuila : left_height + right_height->
            self.maxdiameter = max(self.maxdiameter, left_height + right_height)

            # return the max height to that particular nodex existed -->
            return 1 + max(left_height, right_height)

        


        dfs(root)
        # time : O(n : no. of nodes in the trees->) , space : O(h : height of the trees-->)
        return self.maxdiameter
        

        