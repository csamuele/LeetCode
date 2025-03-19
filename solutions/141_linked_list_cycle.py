# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode | None = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not(head.next):
            return False
        if not(head.next.next):
            return False
        slowPointer = head
        fastPointer = head.next.next
        while fastPointer != slowPointer:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if fastPointer == None:
                return False
        return True
