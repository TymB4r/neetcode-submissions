from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_curr = head
        while old_curr:
            old_curr.next = Node(old_curr.val, old_curr.next, old_curr.random)
            old_curr = old_curr.next.next

        new_head = head.next
        new_curr= new_head
        while new_curr:
            if new_curr.random:
                new_curr.random = new_curr.random.next
            new_curr = new_curr.next

        old_curr, new_curr = head, new_head
        while old_curr:
            old_curr.next = old_curr.next.next
            if new_curr.next:
                new_curr.next = new_curr.next.next
                
            old_curr, new_curr = old_curr.next, new_curr.next

        return new_head