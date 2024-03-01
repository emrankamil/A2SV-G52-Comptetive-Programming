# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        summ = 0
        if not root: return 0

        def traverse(root, cur_sum):
            nonlocal summ
            cur_sum = cur_sum*10+int(root.val)
            if root.left and root.right:
                traverse(root.left, cur_sum)
                traverse(root.right, cur_sum)
            elif root.left:
                traverse(root.left, cur_sum)
            elif root.right:
                traverse(root.right, cur_sum)
            else:
                summ += cur_sum
            

        traverse(root, 0)
        return summ