from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth_next(node: Optional[ListNode], k: int) -> Optional[ListNode]:
            for _ in range(k):
                if not node:
                    return None
                node = node.next
            return node

        if not head: return None
        curr_group_last = get_kth_next(head, k-1)
        if not curr_group_last:
            return head
        new_head = curr_group_last

        # group_tail starts as the first node in the group, but after reversing the window, it becomes the last node
        group_tail, curr = head, head
        while True:
            prev = None
            for _ in range(k):
                curr_next = curr.next
                curr.next = prev
                prev = curr
                curr = curr_next

            future_next_group_first = get_kth_next(curr, k-1)
            if future_next_group_first:
                group_tail.next = future_next_group_first
                group_tail = curr
            else:
                group_tail.next = curr
                return new_head