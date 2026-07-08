"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        n = {}
        curr = head
        while curr:
            n[curr] = Node(curr.val)
            curr = curr.next
        n[None] = None
        curr = head
        while curr:
            n[curr].next = n[curr.next]
            n[curr].random = n[curr.random]
            curr = curr.next
        return n[head]
