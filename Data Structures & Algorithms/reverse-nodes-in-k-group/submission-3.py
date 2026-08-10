from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def kth_next(node: Optional[ListNode], k: int) -> Optional[ListNode]:
            for _ in range(k):
                if not node:
                    return None
                node = node.next
            return node

        if not head: return None
        if not kth_next(head, k-1):
            return head

        new_head = kth_next(head, k-1)
        curr_group_first = head
        curr = head


        while True:
            prev = None
            for _ in range(k):
                curr_next = curr.next
                curr.next = prev
                prev = curr
                curr = curr_next

            group_link = kth_next(curr, k-1)
            if group_link:
                curr_group_first.next = group_link
                curr_group_first = curr
            else:
                curr_group_first.next = curr
                return new_head