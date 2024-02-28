# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(array):
            if len(array) == 0:return
            if len(array) == 1:
                return TreeNode(array[0])

            n = len(array)//2
             
            left = build(array[:n])
            right = build(array[n+1:])
            return TreeNode(array[n], left, right)

        return build(nums)

