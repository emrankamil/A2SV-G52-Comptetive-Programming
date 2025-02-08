# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(i, cur):
            result.append(cur.copy())
            for j in range(i, len(nums)):
                backtrack(j+1, cur + [nums[j]])
        
        backtrack(0, [])
        return result