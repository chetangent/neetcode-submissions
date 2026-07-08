# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = l1, l2
        head = ListNode(c1.val + c2.val)
        c3 = head
        c1 = c1.next
        c2 = c2.next
        while c1 and c2:
            c3.next = ListNode(c1.val + c2.val)
            c1 = c1.next
            c2 = c2.next
            c3 = c3.next
        if c1:
            c3.next = c1
        elif c2:
            c3.next = c2
        c3 = head
        while c3:
            if c3.val > 9:
                c3.val%=10
                if c3.next:
                    c3.next.val+=1
                else:
                    c3.next = ListNode(1)
            c3 = c3.next
        return head