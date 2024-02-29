# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = [(root, 1)]
        rst = 1
        while level:
            next_level = []
            for node, pos in level:
                if node.left:
                    next_level.append((node.left, 2*pos))
                if node.right:
                    next_level.append((node.right, 2*pos+1))
                
            level = next_level
            if level:
                rst = max(rst, level[-1][1]-level[0][1]+1)
        
        return rst

         
