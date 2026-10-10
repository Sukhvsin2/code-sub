# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balanced(root):
            if not root : return -1

            leftTree = balanced(root.left)
            rightTree = balanced(root.right)

            if leftTree == -2 or rightTree == -2:
                return -2

            if abs(leftTree - rightTree) >  1:
                return -2
            return max(leftTree, rightTree)+1
            
        if not root: return True

        return False if balanced(root) == -2 else True