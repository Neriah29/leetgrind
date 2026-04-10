"""
Doubly-linked list node class 
cache dictionary separate 
create insert and remove to run operations on cache 

"""
class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value 
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache, self.cap = {}, capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def insert(self, node):
        node.prev, node.next = self.right.prev, self.right
        node.prev.next = self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])            
        else:
            self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)




        
