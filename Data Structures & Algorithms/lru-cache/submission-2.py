class Node:
    def __init__(self, val, key, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0,0)
        self.store = {}
        
        self.tail.prev = self.head
        self.head.next = self.tail

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_at_beg(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        
    def get(self, key: int) -> int:
        exists = self.store.get(key)
        if exists:
            # move node to MRU
            self.remove(exists)
            self.insert_at_beg(exists)
            return exists.val
        return -1

    def put(self, key: int, value: int) -> None:        
        exists = self.store.get(key) # check if the Node exists

        if exists:
            # remove from the List
            self.remove(exists)
            # move the Node to MRU
            self.insert_at_beg(exists)
            # update the value
            exists.val = value
        else:
            if len(self.store)+1 > self.capacity:
                # remove LRU node
                lru = self.tail.prev
                del self.store[lru.key]
                self.remove(lru)
            
            # add a new key and node to MRU in list
            node = Node(value, key)
            self.store[key] = node
            self.insert_at_beg(node)



