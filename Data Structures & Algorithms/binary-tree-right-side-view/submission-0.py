# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        result = []

        def dfs(node, level):
            
            # base case if not root exists simply return -->
            if not node:
                return

            # if (level == len(result) --> corrosponding to the first node in each level)
            # add(node.val) to the result -->
            # if its the root node then also add it to the the resultant
            # root node will be considered for the right view side view for the tree so far.....
            if (level == len(result)):
                result.append(node.val)


            dfs(node.right, level + 1)


            dfs(node.left, level + 1)



        dfs(root, 0)
        return result

        