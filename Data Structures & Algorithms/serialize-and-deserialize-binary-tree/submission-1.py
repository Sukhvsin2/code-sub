# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def buildPreOrder(self, root, preorder):
        if not root: 
            preorder.append("#")
            return None

        preorder.append(str(root.val))
        self.buildPreOrder(root.left, preorder)
        self.buildPreOrder(root.right, preorder)


    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: 
            return ""
        preorder = []
        self.buildPreOrder(root, preorder)

        return ','.join(preorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "": return None
        values = data.split(',')
        index = 0

        def buildTree(values):
            nonlocal index # using common index to share state b/w calls.
            
            
            if index > len(values)-1: # means we are out of bound
                return None

            val = values[index] # node value to process

            index += 1

            if val == "#": # if value is NULL
                return None

            
            # Create a node
            root = TreeNode(int(val))

            # build left tree
            root.left = buildTree(values)

            # build right tree
            root.right = buildTree(values)
            
            # return root
            return root
        return buildTree(values)

