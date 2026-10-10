# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def rev(head, node):
            if node and node.next == None:
                head.next = node
                return head, node
            
            if node:
                head, curr = rev(head, node.next)  # 3
                curr.next = node
                node.next = None
            return head, node

        tmp = ListNode(0, head)
        head, node = rev(tmp, head)
        return head.next




