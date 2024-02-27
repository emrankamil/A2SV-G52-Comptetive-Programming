class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(cur):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return

            for i in range(len(nums)):
                if nums[i] in cur: continue
                cur.append(nums[i])
                backtrack(cur)
                cur.pop()

        backtrack([])
        return ans