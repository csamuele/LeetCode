# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next: ListNode | None = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

pos5 = ListNode(5)
pos4 = ListNode(-4, pos5)
pos3 = ListNode(0, pos4)

pos2 = ListNode(2, pos3)
pos5.next = pos2
testCase = ListNode(3, pos2)

sol = Solution()

sol.detectCycle(testCase)