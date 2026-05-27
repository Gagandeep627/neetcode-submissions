# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        #  (val --> (Treenode for Inorder_) : i --> (index) for i, val in enumerate(inorder))
        inorder_index = {val: i for i, val in enumerate(inorder)}
        # start preorder_index : 0
        self.preorder_index = 0


        # topic : DFS --> time : O(N : no. of nodes in the trees...). ++ : ++ ??
        def dfs(left, right):
            
            # if (left > right) : terminate the code.. : //
            if (left > right):
                return None


            # evaluate the root_val --> took from preorder[self.preorder_index calculated from 0 th -->]
            root_val = preorder[self.preorder_index]
            # preorder_index : += 1 from the root --> left --> rightest node -->
            self.preorder_index += 1


            # create root TreeNode(corrosponding to the root_val)
            root = TreeNode(root_val)
            # evaluate mid which is equal to index for the root_index -->
            mid = inorder_index[root_val]

            #  root.left will go from DFS traversal for (left , mid - 1) -->
            root.left = dfs(left, mid - 1)
            # root.right will go from DFS traversal for (mid + 1, right) -->
            root.right = dfs(mid + 1, right)
            # : root -->
            return root

        ans = dfs(0, len(inorder) - 1)



        return ans


        
        