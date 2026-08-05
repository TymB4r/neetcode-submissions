class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        new_head = Node(head.val)
        old_curr, new_curr = head, new_head
        old_to_new_node = {None: None, head: new_head}
        cur_idx = 0

        while old_curr.next:
            new_curr.next = Node(old_curr.next.val)
            old_curr, new_curr = old_curr.next, new_curr.next
            old_to_new_node[old_curr] = new_curr
            cur_idx += 1

        old_curr, new_curr = head, new_head
        while old_curr:
            new_curr.random = old_to_new_node[old_curr.random]
            old_curr, new_curr = old_curr.next, new_curr.next

        return new_head