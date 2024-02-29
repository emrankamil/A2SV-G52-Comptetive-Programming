# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelSymmetry(self, level, width):

        if width - level[-1][1] != level[0][1]-1: return False
        for i in range(len(level)//2):
            if level[i][0].val != level[len(level)-i-1][0].val:
                return False
            if width - level[len(level)-i-1][1] != level[i][1]-1:
                return False
            
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        level = [(root, 1)]
        width = 1
        while level:
            n = len(level)
            next_level = []

            if width!=1 and (n%2 or not self.levelSymmetry(level, width)):
                return False
                
            for node, pos in level:
                if node.left: next_level.append((node.left,pos*2-1))
                if node.right: next_level.append((node.right, pos*2))

            level = next_level
            width *= 2

        return True