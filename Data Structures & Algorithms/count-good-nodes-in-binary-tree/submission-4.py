# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:



        def dfs(node, new_max):

            
            if not node:
                return 0
            
            if (node.val >= new_max):
                good = 1
            else:
                good = 0


            new_max = max(node.val, new_max)

            left_good = dfs(node.left, new_max)

            right_good = dfs(node.right, new_max)

            return (good + left_good + right_good)


        ans = dfs(root, root.val) 

        return ans






        

        # dfs(root, 0)
        