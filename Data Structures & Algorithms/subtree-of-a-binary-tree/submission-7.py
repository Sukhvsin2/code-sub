# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def search(root, val):
            
            if not root: return False
            # print(root.val)
            if root.val == val: 
                # print("found it")
                return root

            left = search(root.left, val)
            right = search(root.right, val)

            if left: return left
            if right: return right

            return None

        def isSameTree(p, q):
            if not p and not q: # means we are at leaft node
                return True
            elif not p and q: # missing 1 node from p
                return False
            elif p and not q: # missing 1 node from q
                return False

            # print(p.val, "==", q.val)
            if p.val != q.val: 
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        if not subRoot: return True

        q = deque()
        q.append(root)
        res = False

        while len(q):

            for i in range(len(q)):
                node = q.popleft()

                found_it = search(node, subRoot.val)
                if found_it:
                    res = isSameTree(found_it, subRoot)

                if res:
                    return res
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                

        return res