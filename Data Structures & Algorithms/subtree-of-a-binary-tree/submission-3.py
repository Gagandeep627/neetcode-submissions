# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case if not subroot then subRoot could be considered as valid subtree-->
        if not subRoot:
            return True
        # if not root exists then no subtree exists in the root..
        if not root:
            return False
        # check for the subtree in the tree issamesubtree(root, subroot)-->
        if self.issamesubtree(root, subRoot):
            return True

        # compare for all the left && right nodes of the tree to find out the subtree
        # whether exists there in teh all left subtrees and right sub trees existed so far...
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


    ### helper functions for issubtree(root, subroot) -->
    def issamesubtree(self,root, subroot):
        # if both root && subroot doesnt existed means --> then it is valid symmetry
        if not root and not subroot:
            return True
        # if any of (root, subroot) doesnt existed in the tree &&
        # if root.val != subroot.val then it dowesnt supports symmetry of the 
        # subtree --> return False-->
        if ((not root or not subroot) or (root.val != subroot.val)):
            return False

        # if root.val != subroot.val:
        #     return False

        # check for all root, subroot left nodes and compare it with all 
        # right nodes to check for the symmetry if existed the return --> True -->
        return (self.issamesubtree(root.left, subroot.left) and self.issamesubtree(root.right, subroot.right))
        