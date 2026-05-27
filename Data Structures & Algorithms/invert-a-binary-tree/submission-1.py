# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:



        # topic : brute force:

        if not root:
            return None
        
       
        root.left, root.right = root.right, root.left


        
        self.invertTree(root.left)
        self.invertTree(root.right)


        # time complexity : each node is visited once --> O(n)
        # space complexity : recursion stack --> O(n) (worst case for skewed tress , average O(log(n)))
        # for balanced trees -->
        return root





        