# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        queue = deque([root])
        order = []
        while queue:
            popped = queue[-1]
            if not popped.children:
                order.append(popped.val)
                queue.pop()
            else:
                n = len(popped.children)
                for i in range(n-1, -1, -1):
                    queue.append(popped.children[i])
                popped.children = []
        return order
