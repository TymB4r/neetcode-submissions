from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        right = head
        n = 1
        while right.next:
            n += 1
            right = right.next

        prev = None
        curr = head
        nxt = head.next

        curr_idx = 0
        while curr:
            nxt = curr.next
            if curr_idx == n // 2:
                curr.next = None # Disconnect the middle node to avoid making a cycle
            elif curr_idx > n // 2:
                curr.next = prev
            prev = curr
            curr = nxt
            curr_idx += 1

        left = head

        visited = 1  # left is by default the first node in the new linked-list
        while visited < n:
            l_nxt = left.next
            left.next = right
            left = l_nxt
            visited += 1

            if visited == n:
                break

            r_nxt = right.next
            right.next = left
            right = r_nxt
            visited += 1

        return None