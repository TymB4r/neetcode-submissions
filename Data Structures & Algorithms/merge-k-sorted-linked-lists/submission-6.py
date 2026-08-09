from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next

        curr = head

        while list1 and list2:
            # if not list1:
            #     curr.next = list2
            #     return head
            # if not list2:
            #     curr.next = list1
            #     return head

            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next

            curr = curr.next
        curr.next = list1 if list1 else list2
        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        n = len(lists)
        while n > 1:
            i = 0
            write_idx = 0
            while i + 1 < n:
                lists[write_idx] = self.mergeTwoLists(lists[i], lists[i + 1])
                write_idx += 1
                i += 2
            if i == n - 1:
                lists[write_idx] = lists[i]
            n = (n + 1) // 2

        return lists[0]