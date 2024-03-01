# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            max_idx = 0
            for i, val in enumerate(nums):
                if val > nums[max_idx]:
                    max_idx = i
            root = TreeNode(nums[max_idx])
            root.left = self.constructMaximumBinaryTree(nums[:max_idx])
            root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
            return root