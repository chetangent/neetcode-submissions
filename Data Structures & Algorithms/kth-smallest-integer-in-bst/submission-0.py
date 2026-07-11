# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = [root]
        curr = root
        while q:
            if curr.left:
                curr = curr.left
                q.append(curr)
            else:
                node = q.pop()
                k-=1
                if not k:
                    return node.val
                if node.right:
                    curr = node.right
                    q.append(curr)