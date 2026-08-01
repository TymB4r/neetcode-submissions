class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        prev = None
        while curr.next:
            next_ele = curr.next
            curr.next = prev
            prev = curr
            curr = next_ele

        curr.next = prev

        return curr