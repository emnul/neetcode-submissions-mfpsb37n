class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key -> Node

        self.lru, self.mru = Node(0,0), Node(0,0)
        self.lru.next, self.mru.prev = self.mru, self.lru

    # remove from linked list
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    # insert at mru
    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from LL and del LRU from cache
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]
        
