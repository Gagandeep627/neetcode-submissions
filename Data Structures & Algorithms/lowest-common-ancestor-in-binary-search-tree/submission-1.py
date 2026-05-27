# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # topic : DFS (binary search Trees... ++)
        if not root:
            return None

        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)

        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)

        else:
            return root


        # time : O(H), space : O(H).... : ??

        
        
# the worst case, we might go all the way to a leaf.
# 👉 Time Complexity = O(h)
# where h = height of the BST


# In the worst case, recursion depth = height of tree
# 👉 Space Complexity = O(h)

        
