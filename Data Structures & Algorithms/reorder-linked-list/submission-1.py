# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        prev = None
        curr = temp
        while curr and curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        if curr:
            curr.next = prev
        c1, c2 = head.next, temp
        c3 = head
        while c1 and c2:
            c3.next = c2
            c3 = c3.next
            c2 = c2.next
            c3.next = c1
            c1 = c1.next
            c3 = c3.next
