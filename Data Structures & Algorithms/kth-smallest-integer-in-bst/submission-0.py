# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root, items):
            if not root:
                return root

            inorder(root.left, items)
            items.append(root.val)
            inorder(root.right, items)

        items = []
        inorder(root, items)
        return items[k-1]