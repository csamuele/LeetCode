
class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def removeNode(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insertNode(self, node):
        next = self.right
        prev = self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.insertNode(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.removeNode(self.cache[key])
        self.cache[key] = node = Node(key, value) 
        self.insertNode(node)
        if len(self.cache) > self.capacity:
            lruNode = self.left.next
            self.removeNode(lruNode)
            del self.cache[lruNode.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)