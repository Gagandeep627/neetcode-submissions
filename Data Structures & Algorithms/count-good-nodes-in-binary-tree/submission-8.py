# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        # topic : DFS -->
        def dfs(node, new_max):

            # base case if not node exists -->
            if not node:
                return 0
            
            # good count to be returned for that node == 1 if (node.val > max_so_far calculated till now... else : good : 0).. : //
            good = 1 if (node.val >= new_max) else 0
            # new_max --> max(node.val, new_max)
            new_max = max(node.val, new_max)
            # similary recursively call for all left nodes of the root node existed so far...
            left_good = dfs(node.left, new_max)
            # similary recursively call for all right nodes of the root node existed so far...
            right_good = dfs(node.right, new_max)

            # values (good for current node and all the left nodes for the subtrees && right nodes for the subtrees and are returned : (good + left_good + right_good))
            return (good + left_good + right_good)

        # recursively : dfs(root.node, root.val)
        ans = dfs(root, root.val) 

        return ans






        

        # dfs(root, 0)
        