# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last_nodes = []
        def search(root):
            nonlocal last_nodes
            if root:
                if not search(root.left): return False
                
                last_nodes.append(root.val)
                if len(last_nodes)>1:
                    if last_nodes[-1]<=last_nodes[-2]: return False
                    last_nodes = [last_nodes[-2], last_nodes[-1]]

                if not search(root.right): return False

            return True

        return search(root)