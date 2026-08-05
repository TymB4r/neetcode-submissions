class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_curr = head
        while old_curr:
            old_curr.random = Node(old_curr.val, old_curr.next, old_curr.random) # Temporarily store the deep copied nodes in random
            old_curr = old_curr.next

        new_head = head.random
        old_curr, new_curr = head, new_head

        while old_curr.next:
            if new_curr.random:
                new_curr.random = new_curr.random.random
            new_curr.next = old_curr.next.random
            old_curr, new_curr = old_curr.next, new_curr.next
        if new_curr.random:
            new_curr.random = new_curr.random.random

        return new_head