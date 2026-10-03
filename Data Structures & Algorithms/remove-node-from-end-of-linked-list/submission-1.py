# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head

        # create a gap b/w l and r
        while r and n:
            n -= 1
            r = r.next

        if r == None:
            head = head.next
            return head

        prev = None
        while r:
            prev = l
            l = l.next
            r = r.next

        prev.next = l.next

        return head

