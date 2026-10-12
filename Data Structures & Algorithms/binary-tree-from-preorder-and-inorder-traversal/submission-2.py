# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursion gives time out error.
class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     if inorder:

    #         mid = inorder.index(preorder.pop(0))
    #         root = TreeNode(inorder[mid])
    #         root.left = self.buildTree(preorder, inorder[:mid])
    #         root.right = self.buildTree(preorder, inorder[mid+1:])
    #         return root
    #     # return None




    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # O(n) preprocessing
        index_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def build(left, right):
            nonlocal pre_idx

            if left > right:
                return None

            # Get next root from preorder
            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)

            # O(1) lookup
            mid = index_map[root_val]

            # Construct left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)