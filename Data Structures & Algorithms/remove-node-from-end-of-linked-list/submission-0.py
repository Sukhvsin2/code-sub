# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n==1:
            return None
        
        # brute force
        # reverse the list
        # traverse N times remove it and then reverse the list again
        # return the head

        # reverse the list
        prev, curr = None, head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head = prev
        curr = prev

        # remove the nth node
        for i in range(n-1):
            prev = curr
            curr = curr.next
        
        # remove/skip the node
        if n == 1:        
            head = head.next
        else:
            prev.next = curr.next

        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head = prev

        return head