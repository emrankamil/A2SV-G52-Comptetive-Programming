# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        rst = 0
        def dfs(node, d, dis):
            nonlocal rst
            if not (node.right or node.left):
                return {d:1}

            l_leafs = r_leafs = {}
            if node.left:
                l_leafs = dfs(node.left, d + 1, dis)
            if node.right:
                r_leafs = dfs(node.right, d + 1, dis)
            
            for i in l_leafs:
                for j in r_leafs:
                    if i + j - 2*d <= dis:
                        rst += l_leafs[i] * r_leafs[j]
                
            for i in r_leafs:
                if i not in l_leafs:
                    l_leafs[i] = r_leafs[i]
                else:
                    l_leafs[i] += r_leafs[i]

            return l_leafs

        dfs(root, 1, distance)
        return rst