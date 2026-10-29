class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class PrefixTree:

    def __init__(self):
        self.rootNode = Node()
        

    def insert(self, word: str) -> None:
        cur = self.rootNode
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
        
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.rootNode

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.rootNode

        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        
        return True
        