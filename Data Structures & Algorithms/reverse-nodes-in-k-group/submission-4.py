# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def display(head):
            curr = head
            items = []
            while curr:
                items.append(str(curr.val))
                curr = curr.next

            print(" -> ".join(items))

        def traverse(curr, k):
            while curr and k > 0:
                curr = curr.next
                k-=1

            return curr

        
        def reverse(head, tail):
            prev = None
            while head and head != tail:
                next = head.next
                head.next = prev
                prev = head
                head = next

            return prev, tail


        dummy = ListNode(0, head)
        groupPrev = dummy
        curr = dummy

        while True:

            getkth = traverse(curr, k)

            if getkth == None:
                break


            
            groupPrev = curr.next
            groupNext = getkth.next

            curr.next, tail = reverse(curr.next, groupNext) # groupPrev become a new head
            
            groupPrev.next = tail
            curr = groupPrev

        return dummy.next



