# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head,tail = None, None

        while list1 and list2:   # traverse both which
            # compare elements from both
            if list1.val < list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
            
            if head: # if head has some node
                tail.next = ListNode(val)
                tail = tail.next
            else:
                head = ListNode(val)
                tail = head

        while list1:    # if list1 has left nodes
            if head:
                tail.next = ListNode(list1.val)
                tail = tail.next
            else:
                head = ListNode(list1.val)
                tail = head

            list1 = list1.next


        while list2:    # if list2 has left nodes
            if head:
                tail.next = ListNode(list2.val)
                tail = tail.next
            else:
                head = ListNode(list2.val)
                tail = head
        
            list2 = list2.next
        return head