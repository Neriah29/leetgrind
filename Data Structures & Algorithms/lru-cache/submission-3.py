"""
Design
Doubly-linked list

get -> hashmap

put -> hashmap & linked list

move_to_front method
remove method
"""
#Doubly-linked list
class Node:
    def __init__(self, key = None, value = None, next = None, prev = None):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev


class LRUCache:
    #init empty linked list, hashmap and capacity
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right, self.left = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

        

    def get(self, key: int) -> int:
        #check cache
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key]) #remove the node if alr in the list

        if len(self.cache) >= self.capacity:
            self._remove(self.left.next)
        
        self._add(Node(key, value))
    
    def _remove(self, node):
        #rem from cache
        self.cache.pop(node.key)

        #rem from linked list
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node
    
    def _add(self, node): #moves the node to the front of list, and reassigns key
        #_add to cache:
        self.cache[node.key] = node

        #move to mru node
        prev_top_node = self.right.prev
        prev_top_node.next, node.prev = node, prev_top_node
        node.next, self.right.prev = self.right, node

        





