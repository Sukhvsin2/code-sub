# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_ll(list1, list2):
            head = ListNode(0)
            curr = head
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next

            if list1:
                curr.next = list1
            
            if list2:
                curr.next = list2

            return head.next

        
        def merge_range(left, right):
            if left == right:
                return lists[left]

            mid = (left+right)//2

            left_list = merge_range(left, mid)
            right_list = merge_range(mid+1, right)

            return merge_ll(left_list, right_list)
        
        return merge_range(0, len(lists)-1)
        