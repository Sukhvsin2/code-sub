# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the list
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # once above traversing done slow is pointing to mid of the list.
        list2 = slow.next   # 2nd list starting
        slow.next = None

        # reverse the 2nd list?
        prev, curr, next_node = None, list2, None
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # list2 reversed
        list2 = prev

        # merge both LL
        first, second = head, list2

        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1

            first, second = t1, t2

        

