# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:



        self.count = 0
        self.result = 0


        # topic : DFS time : O(N) 
        def dfs(node):
            # if not node : return None -->
            if not node:
                return

            # do inorder traversal --> traverse towards 
            # traverse towards left nodes reach towards left most then  
            dfs(node.left)
            # start count from the left most node to the 
            # root --> wherever the count --> K then store the result
            # in the K --> store the self.result --> node.val -->
            self.count += 1

            if (self.count == k):
                self.result = node.val

            # then from traversing from the root go to the rightmost node,
            # this the concept for Inorder traversal to return 
            # nodes from the leftmost nodes --> rightmost nodes -->
            dfs(node.right)


        dfs(root)

        return self.result








        