from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        slow, fast = head, head
        n = 1
        while fast.next:
            fast, slow = fast.next, slow.next
            n += 1
            if not fast.next:
                break

            fast = fast.next
            n += 1

        nxt = slow.next
        slow.next = None # Disconnect the left and right partitions

        while slow:
            prev = slow
            if not nxt:
                break
            slow = nxt
            nxt = slow.next
            slow.next = prev

        joined = 1 # The new order takes the old order's first element as its first

        left, right = head, slow
        while joined < n:
            left_next = left.next
            left.next = right
            left = left_next
            joined += 1
            if joined == n:
                break

            right_next = right.next
            right.next = left
            right = right_next
            joined += 1

        return None