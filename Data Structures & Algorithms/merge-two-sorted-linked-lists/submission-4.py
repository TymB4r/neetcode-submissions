from typing import Optional


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
                if list1.val > list2.val:
                    curr.next = list2
                    list2 = list2.next
                else:
                    curr.next = list1
                    list1 = list1.next

                curr = curr.next

            curr.next = list1 if list1 else list2
            return head