# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head,tail = None, None
        
        head = ListNode()
        tail = head

        while list1 and list2:   # traverse both which
            node = None
            # compare elements from both
            if list1.val < list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
            
            tail.next = node
            tail = tail.next

        while list1:    # if list1 has left nodes
            tail.next = list1
            tail = tail.next
            list1 = list1.next


        while list2:    # if list2 has left nodes
            tail.next = list2
            tail = tail.next    
            list2 = list2.next

        return head.next