# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        fast = head.next
        prevSlow = None
        slow = head
        nextSlow = slow.next
        slow.next = prevSlow
        maxSum = 0
        while fast and fast.next:
            fast = fast.next.next
            prevSlow = slow
            slow = nextSlow
            nextSlow = slow.next
            slow.next = prevSlow
        leftHead = slow
        rightHead = nextSlow
        while leftHead and rightHead:
            maxSum = max(maxSum, leftHead.val + rightHead.val)
            leftHead = leftHead.next
            rightHead = rightHead.next
        return maxSum

