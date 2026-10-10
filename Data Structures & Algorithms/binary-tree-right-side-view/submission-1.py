# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        q = deque()
        res = []

        q.append(root)
        res.append(root.val)

        while len(q):
            temp = []

            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    temp.append(node.left.val)
                    q.append(node.left)
                
                if node.right:
                    temp.append(node.right.val)
                    q.append(node.right)
            
            if temp:
                res.append(temp[-1])

        return res
