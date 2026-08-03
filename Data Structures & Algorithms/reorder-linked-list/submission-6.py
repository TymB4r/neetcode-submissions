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
        cur_idx = 0

        while cur_idx < n // 2:
            prev = curr
            curr = curr.next
            cur_idx += 1
            
        while curr:
            nxt = curr.next
            if cur_idx == n // 2:
                curr.next = None  # Disconnect the left and right parts to avoid making a cycle
            elif cur_idx > n // 2:
                curr.next = prev
            prev = curr
            curr = nxt
            cur_idx += 1

        left = head
        new_connected = 1  # left is by default the first node in the new linked-list
        while new_connected < n:
            l_nxt = left.next
            left.next = right
            left = l_nxt
            new_connected += 1

            if new_connected == n:
                break

            r_nxt = right.next
            right.next = left
            right = r_nxt
            new_connected += 1

        return None