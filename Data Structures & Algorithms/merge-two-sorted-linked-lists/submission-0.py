# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = list1, list2
        if not c1 and not c2:
            return None
        elif not c1:
            return c2
        elif not c2:
            return c1
        if c1.val < c2.val:
            head = c1
            c1 = c1.next
        else:
            head = c2
            c2 = c2.next
        c3 = head
        while c1 and c2:
            if c1.val < c2.val:
                c3.next = c1
                c1 = c1.next
                c3 = c3.next
            else:
                c3.next = c2
                c2 = c2.next
                c3 = c3.next
        if c1:
            c3.next = c1
        elif c2:
            c3.next = c2
        return head