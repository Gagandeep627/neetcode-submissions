# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:



        # topic : DFS-->
        def dfs(node, low, high):

            # if reached to empty node : return True -->
            if not node:
                return True


            # condn for BST Tree --> node.val should be greater than low && 
            # less than high -->
            if not (low < node.val < high):
                return False
            
            # evaluate --> same way for left nodes set low to already : "-inf" to same and highest value will be the high : node.val
            left_is_valid = dfs(node.left, low, node.val)

            # evaluate for right nodes --> similarly and set low : node.val as it will be the smallest for the node.right.val
            # and high already assigned to "+inf"
            right_is_valid = dfs(node.right, node.val, high)


            # if both (left) and (right) subtrees satisfies the condition for being a 
            # a valid node in the BST as per the BST condition then --> 
            # this statement will return True else : False if traversing though all left && right nodes
            # for both subtrees it is able to reach the empty (Null) node --> it will return 
            # True -->
            return ((left_is_valid) and (right_is_valid))

        # low : -inf , high : +inf, root : root-->

        # time : O(n : no. of nodes)
        # space : O(H : height of the : O(n) : for skewed tree --> O(log(n) --> for a balanced trees))-->
        ans = dfs(root, float("-inf"), float("+inf"))
        return ans