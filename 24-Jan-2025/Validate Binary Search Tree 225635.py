# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBST(root, valid_range):   
            if root.val <= valid_range[0] or root.val >= valid_range[1]:
                return False
            if root.right: 
                result = checkBST(root.right, (root.val, valid_range[1]))
                if not result:
                    return False
            if root.left:
                result = checkBST(root.left, (valid_range[0], root.val))
                if not result:
                    return False

            return True

        if not root:
            return True
        checkBST(root, (-float('inf'), float('inf')))

        return checkBST(root, (-float('inf'), float('inf')))