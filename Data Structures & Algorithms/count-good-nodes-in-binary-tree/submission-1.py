# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def good(root, val):
            if not root: return 0

            # print(root.val)
            if val <= root.val:
                # good node
                # print("good node and max so far ", root.val)
                left = good(root.left, root.val)
                right = good(root.right, root.val)
                return 1 + left + right
            else:
                # bad node since passed val is smaller than the root.val
                # print("bad node and max so far ", val)
                left = good(root.left, val)
                right = good(root.right, val)
                return left + right
                
        return good(root, root.val)
        # return 0

        
