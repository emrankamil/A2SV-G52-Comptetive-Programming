class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        rst = []
        last = 0
        def backtrack(start, cur, cur_sum):
            nonlocal last
            if cur_sum == target:
                rst.append(cur[:])
                return 
            elif cur_sum > target:return

            for i in range(start, len(candidates)):
                if i>0 and candidates[i]==last:continue
                cur.append(candidates[i])
                cur_sum += candidates[i]
                backtrack(i+1, cur, cur_sum )
                last = cur.pop()
                cur_sum -= candidates[i]

        candidates.sort(reverse=True)
        backtrack(0, [], 0)
        return rst
