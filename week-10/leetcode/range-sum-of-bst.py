# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        count = 0
        def search(root):
            nonlocal count
            if root:
                left = search(root.left)
                if left and left.val >= low and left.val <= high:
                    count += left.val
                elif left and left.val > high:return

                if root.val >= low and root.val <= high:
                    count += root.val
                elif root.val > high: return

                right = search(root.right)
                if right and right.val >= low and right.val <= high:
                    count += right.val
                elif right and right.val > high:return
        search(root)
        return count