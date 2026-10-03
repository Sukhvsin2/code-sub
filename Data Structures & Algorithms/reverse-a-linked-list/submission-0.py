# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:

            prev, curr, next_node = None, head, None

            while curr:
                next_node = curr.next   # save next node
                curr.next = prev        # reverse the link
                prev = curr             # save the prev state
                curr = next_node        # move to next node

            head = prev                 # prev holds the last node

        return head