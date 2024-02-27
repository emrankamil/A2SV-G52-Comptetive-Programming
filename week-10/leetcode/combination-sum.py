class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sum = 0
        rst = []
        subArray = []

        def dfs(sum, subArray, cand):
            nonlocal rst
            if sum == target:
                rst.append(subArray.copy())
                return 
            elif sum > target or len(cand)==0:
                return 
            else:
                for i in range(len(cand)):
                    sum += cand[i]
                    subArray.append(cand[i])
                    dfs(sum,subArray,cand[i:])
                    sum -= cand[i]
                    subArray.pop()
        
        dfs(0,subArray,candidates)
        return rst


