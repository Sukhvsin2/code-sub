"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None: None}
        curr = head

        # new nodes creted and saved the addrs in hashmap
        while curr:
            hashmap[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        # map saved nodes
        while curr:
            hashmap[curr].next = hashmap[curr.next]
            hashmap[curr].random = hashmap[curr.random]

            curr = curr.next

        return hashmap[head]