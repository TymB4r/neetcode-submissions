from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        back, front = head, head

        for _ in range(n):
            front = front.next

        if not front:
            return head.next # Remove the first element

        while front.next:
            front = front.next
            back = back.next

        back.next = back.next.next
        return head