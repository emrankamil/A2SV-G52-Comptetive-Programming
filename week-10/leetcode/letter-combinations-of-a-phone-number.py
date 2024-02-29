class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        rst = []
        if len(digits)==0:return []
        
        def backtrack(start, cur):
            if len(cur)==len(digits):
                rst.append("".join(cur[:]))
                return 
            for i in range(start, len(digits)):
                for j in nums[int(digits[i])-2]:
                    cur.append(j)
                    backtrack(i+1, cur)
                    cur.pop()
        
        backtrack(0, [])
        return rst