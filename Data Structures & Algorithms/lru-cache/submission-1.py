"""
data structures:
doubly linked list -> impl node
cache --> dictionary

init:
    left and right fixed

get:
    cache

put:
    check the length of dict, 
    access correct node and del
"""

class Node:
    def __init__(self, value = 0, next = None, prev = None):
        self.val = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        #capacity, cache map, fixed left and right 
        self.capacity = capacity
        self.cache = {}
        self.right, self.left = Node(), Node()
        #left and right point to each other
        self.left.next, self.right.prev = self.right, self.left
        

    def get(self, key: int) -> int:
        #we are just looking for the value of the key 
        if key in self.cache:
            return self.cache[key]
        else:
            return -1
        
    def _remove_lru(self):
        #to remove the lru, we remove the entry from the cache and make left point to the next
        lru_node = self.left.next
        del self.cache[lru_node.val]

        new_lru_node = lru_node.next
        self.left.next = new_lru_node
        new_lru_node.prev = self.left

        
    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity:
            self._remove_lru()

        #regardless we will add
        self.cache[key] = value #added to the cache
        added_node = Node(key)
        top_node = self.right.prev
        top_node.next, added_node.prev = added_node, top_node
        added_node.next, self.right.prev = self.right, added_node



        
