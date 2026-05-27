# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.ans = float("-inf")

        # if not root.left and not root.right:
        #     return root.val


        def dfs(node):

            if not node:
                return 0


            left = max(0, dfs(node.left))

            right= max(0 , dfs(node.right))
            
            # update self.answer to the maximum :
            self.ans = max(self.ans,left + right + node.val)

            # return maximum single node path to the parent node:

            return node.val + max(left, right)


        dfs(root)


        return self.ans



        