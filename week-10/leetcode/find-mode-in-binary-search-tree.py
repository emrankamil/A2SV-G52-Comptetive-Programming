# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mp = defaultdict(int)

        def searchMode(root):
            if root:
                searchMode(root.left)
                mp[root.val] += 1
                searchMode(root.right)

        searchMode(root)
        rst = []
        cur_max = 0
        for i in mp:
            if mp[i] > cur_max:
                rst = [i]
                cur_max = mp[i]
            elif mp[i] == cur_max:
                rst.append(i)

        return rst



# if root.val != last_val:
#     print(root.val)
#     if cur_freq == max_freq:
#         rst.append(last_val)
#     elif cur_freq > max_freq:
#         rst = [last_val]
#         max_freq = cur_freq
#     cur_freq = 0
# else:
#     cur_freq += 1
#     if not root.left and not root.right:
#         if cur_freq > max_freq: rst = [root.val]
#         elif cur_freq == max_freq: rst.append(root.val)
#         return rst
# last_val = root.val
# print(last_val)