# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # resultant to store nodes --> root -->
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

            # trvaerse towards right subtrees first
            dfs(node.right, level + 1)

            # then backtrack and look out for if any yet right subtrees left for the remaianing skewed trees-->
            dfs(node.left, level + 1)


        # ⏱️ Time Complexity → O(n)
        # 💾 Space Complexity → O(h) (recursive stack)

# In the worst case (skewed tree), height h = n, → O(n)

# In the best case (balanced tree), height h = log n, → O(log n)
        dfs(root, 0)
        return result

        