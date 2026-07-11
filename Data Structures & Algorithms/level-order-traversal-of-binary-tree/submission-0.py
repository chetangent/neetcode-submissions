# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use deque
        
        res = []
        if not root:
            return res
        q = [root]
        while q:
            row = []
            l = len(q)
            for i in range(l):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                row.append(q[0].val)
                q.pop(0)
            res.append(row)
        return res