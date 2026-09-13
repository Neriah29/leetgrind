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
    def __init__(self, key = 0, value = 0, next = None, prev = None):
        self.key = key
        self.next = next
        self.prev = prev
        self.val = value

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
            self._move_to_front(self.cache[key])
            return self.cache[key].val
        else:
            return -1


    def _move_to_front(self, node):
        cur_prev, cur_next = node.prev, node.next
        cur_prev.next, cur_next.prev = cur_next, cur_prev

        top_node = self.right.prev
        top_node.next, node.prev = node, top_node
        node.next, self.right.prev = self.right, node


        
    def _remove_lru(self):
        #to remove the lru, we remove the entry from the cache and make left point to the next
        lru_node = self.left.next
        self.cache.pop(lru_node.key)

        new_lru_node = lru_node.next
        self.left.next = new_lru_node
        new_lru_node.prev = self.left

        
    def put(self, key: int, value: int) -> None:
        while len(self.cache) >= self.capacity:
            self._remove_lru()

        #regardless we will add
        cur_node = Node(key, value)
        self.cache[key] = cur_node #added to the cache
        added_node = cur_node
        top_node = self.right.prev
        top_node.next, added_node.prev = added_node, top_node
        added_node.next, self.right.prev = self.right, added_node



        
