# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def singleLevel(queue):
            cur = []
            n = len(queue)
            for _ in range(n):
                popped = queue.popleft()
                cur.append(popped.val)
                if popped.left: queue.append(popped.left)
                if popped.right:  queue.append(popped.right)
            return cur

        queue = deque()
        if not root:
            return []
            
        queue.append(root)
        rst = []
        while queue: # this os O(depth) operation 
            rst.append(singleLevel(queue)) # this is O(elements in a single depth) operation
        #  total O(n) since we are visiting each element only once

        return rst