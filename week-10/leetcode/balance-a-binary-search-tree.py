# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []
        def inorder(root):
            if root:
                inorder(root.left)
                values.append(root.val)
                inorder(root.right)
        
        def balance(values):
            n = len(values)
            if n:
                return TreeNode(values[n//2], balance(values[:n//2]), balance(values[n//2+1:]))
        
        inorder(root)
        return balance(values)