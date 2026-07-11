# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        l = root
        while True:
            if p.val < l.val and q.val < l.val:
                l = l.left
            elif p.val > l.val and q.val > l.val:
                l = l.right
            else:
                break
        return l