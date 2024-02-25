# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque()
        queue.append(root)
        rst , level = [], 0

        while queue:
            rst.append(self.singleLevelTraversal(queue, level))
            level += 1
        return rst

    def singleLevelTraversal(self, queue, level):
        n = len(queue)
        cur = []
        for _ in range(n):
            if level%2:
                popped = queue.popleft()
                if popped.right: queue.append(popped.right)
                if popped.left: queue.append(popped.left)
            else:
                popped = queue.pop()
                if popped.left: queue.appendleft(popped.left)
                if popped.right: queue.appendleft(popped.right)
            cur.append(popped.val)
        return cur

        
        