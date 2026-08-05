class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new_head = Node(head.val)
        old_curr, new_curr = head, new_head
        old_address_to_idx, new_idx_to_address = {None: None}, {None: None}
        cur_idx = 0
        while old_curr.next:
            new_curr.next = Node(old_curr.next.val)
            old_address_to_idx[old_curr] = cur_idx
            new_idx_to_address[cur_idx] = new_curr
            cur_idx += 1
            old_curr, new_curr = old_curr.next, new_curr.next
        old_address_to_idx[old_curr] = cur_idx
        new_idx_to_address[cur_idx] = new_curr

        old_curr, new_curr = head, new_head

        while old_curr:
            random_idx = old_address_to_idx[old_curr.random]
            new_curr.random = new_idx_to_address[random_idx]

            old_curr, new_curr = old_curr.next, new_curr.next

        return new_head