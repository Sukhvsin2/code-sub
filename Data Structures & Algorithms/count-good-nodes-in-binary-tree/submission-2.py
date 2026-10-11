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

            count = 0

            if val <= root.val:
                count = 1

            new_max = root.val if count else val
            
            left = good(root.left, new_max)
            right = good(root.right, new_max)
            return count + left + right
                
        return good(root, root.val)

        
