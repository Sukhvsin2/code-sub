# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def traverse(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1

            return curr
            
        
        def reverse(curr, tail):
            prev = None
            while curr and curr != tail:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        
        dummy = ListNode(0, head)
        prev = dummy
        while True:
            groupPrev = prev
            getkth = traverse(prev, k)

            if getkth == None:
                break
            
            groupNext = getkth.next
            tail = groupPrev.next
            groupPrev.next = reverse(prev.next, groupNext)
            

            # last
            prev = tail
            tail.next = groupNext
        return dummy.next
            