class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        right = head
        n = 1
        while right.next:
            n += 1
            right = right.next

        curr = head
        cur_idx = 0

        while cur_idx < n // 2:
            curr = curr.next
            cur_idx += 1

        prev = curr
        nxt = curr.next
        curr.next = None
        while curr:
            curr = nxt
            if curr:
                nxt = curr.next
            else:
                break
            curr.next = prev
            prev = curr



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