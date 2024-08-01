# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        rst = []
        queue = deque([root])
        while queue:
            n = len(queue)
            rst.append(queue[-1].val)
            for i in range(n):
                popped = queue.popleft()
                if popped.left: queue.append(popped.left)
                if popped.right: queue.append(popped.right)
        return rst