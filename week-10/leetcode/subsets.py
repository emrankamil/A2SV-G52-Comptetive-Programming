class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rst = []
        def backtrack(i, cur):
            rst.append(cur[:])

            for i in range(i, len(nums)):
                cur.append(nums[i])
                backtrack(i+1, cur)
                cur.pop()

        backtrack(0, [])
        return rst