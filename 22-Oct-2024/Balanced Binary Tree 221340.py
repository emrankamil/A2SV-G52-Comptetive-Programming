# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, depth):
            if not root:
                return True, depth
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)

            if not left[0] or not right[0]:
                return False, depth
            
            # Check if the current node's subtrees differ in depth by more than 1
            if abs(left[1] - right[1]) >= 2:
                return False, depth
            
            # Return True and the maximum depth of the subtrees
            return True, max(left[1], right[1])
        
        return dfs(root, 0)[0]
