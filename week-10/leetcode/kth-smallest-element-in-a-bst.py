# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rst = []
        counter = 1
        def search(root, k):
            nonlocal counter, rst
            if root:
                left = search(root.left, k)      
                if left:
                    return left

                if counter == k:
                    rst.append(root.val)
                else:
                    counter += 1
                
                if rst: return rst[0]
                rst = []

                right = search(root.right, k)
                if right:
                    return right

        return search(root, k)