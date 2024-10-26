class ListNode():
    def __init__(self, val:int = 0, next = None, prev = None):
        self.val = val
        self.next:ListNode = next
        self.prev:ListNode = prev

class MyLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        node = ListNode(next=self.head)
        while node and index > 0:
            node = node.next
            index -= 1
        return node.next.val


        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val, self.head)
        if self.head:
            self.head.prev = newNode
        else:
            self.tail = newNode
        self.head = newNode
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val, prev=self.tail)
        if self.tail:
            self.tail.next = newNode
        else:
            self.head = newNode
        self.tail = newNode

        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        
        node = ListNode(next=self.head)
        if index == 0:
            self.addAtHead(val)
            return
        while index >= 0:
            if node.next:
                node = node.next
                index -= 1
            else:
                if index == 0:
                    self.addAtTail(val)
                    return
                else:
                    raise Exception('Index out of range')
        newNode = ListNode(val, node, node.prev)
        node.prev.next = newNode
        node.prev = newNode




    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        node = ListNode(next = self.head)
        while index >= 0:
            if node.next:
                node = node.next
                index -= 1
            else:
                raise Exception("index out of range")
        nextNode = node.next
        prevNode = node.prev
        if nextNode:
            nextNode.prev = prevNode
        if prevNode:
            prevNode.next = nextNode
        
        


# Your MyLinkedList object will be instantiated and called as such:
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)   #linked list becomes 1->2->3
myLinkedList.get(1)             #return 2
myLinkedList.deleteAtIndex(1);  #now the linked list is 1->3
myLinkedList.get(1)             #return 3