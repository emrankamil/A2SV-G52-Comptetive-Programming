class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rst = []
        def backtrack(start, cur, target):
            if target == 0:
                rst.append(cur[:])

            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    cur.append(candidates[i])
                    backtrack(i, cur, target-candidates[i])
                    cur.pop()
        
        backtrack(0, [], target)
        return rst