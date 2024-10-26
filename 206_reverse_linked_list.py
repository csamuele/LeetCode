# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head:ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        previousNode, currentNode = None, head
        while currentNode:
            previousNode = ListNode(currentNode.val, previousNode)
            currentNode = currentNode.next
        return previousNode


#Recursive
class Solution:
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

testNode = ListNode(1, ListNode(2, ListNode(3)))
solution = Solution()
solution.reverseList(testNode)