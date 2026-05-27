# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # result to store the nodes corrosponding to each of the levels -->
        result = []

        # topic : brute force --> O(n)

        def dfs(node, level):

            # if not node exists --> return -->
            if not node:
                return

            if (len(result) == level):
                result.append([])
            # add the node.val to the result[index : level]
            result[level].append(node.val)

            # move the recursion to --> left, (level + 1)
            dfs(node.left, level + 1)

            # move the recursion to --> right, (level + 1)
            dfs(node.right, level + 1)


        # set level for root initially to be --> 0
        dfs(root, 0)

        # time : O(n : no. of nodes in the trees...)
        # space : O(n)
        # return resultant --> all the nodes accnd to their corroponding levels -->
        return result



        