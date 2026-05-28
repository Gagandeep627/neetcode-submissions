# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        # serialize a tree into a string:
        # storinhg serialized values
        result =  []


        # dfs function for preorder traversal:
        def dfs(node):
            
        # if node is null:
            if not node:
                # store "null" for null node
                result.append("Null")
                # stop recursion
                return
            
            # store the current node.value
            result.append(str(node.val))

            # go tp left node.value
            dfs(node.left)
            # go to right node.value
            dfs(node.right)

        # starts dfs from root
        dfs(root)


        return ",".join(result)



    # Decodes your encoded data to tree.
    # deserialize string back into tree:
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # split string into commas
        values = data.split(",")
        # pointer to track current_index
        self.index = 0 
        


        def dfs():
            
            # if null node encountered 
            if values[self.index] == "Null":
                self.index += 1
                return None

            # create node
            node = TreeNode(int(values[self.index]))
            self.index += 1

            # build left subtree
            node.left = dfs()

            # build right subtree
            node.right = dfs()

            # return compeleted node
            return node

        # starts rebuilding tree:
        return dfs()






















        