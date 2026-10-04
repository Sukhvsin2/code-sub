# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        carry = 0
        dummy = ListNode(0)
        tail = dummy

        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = 0
            if val > 9:
                carry = 1
                val -= 10
            tail.next = ListNode(val)
            tail = tail.next
            
        if carry:
            tail.next = ListNode(carry)

        return dummy.next