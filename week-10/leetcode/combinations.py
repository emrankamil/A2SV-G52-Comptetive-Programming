class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtrack(start, cur):
            if len(cur) == k:
                ans.append(cur[:])
                return
            need = k-len(cur)
            remain = n-start+1
            availabe = remain-need

            for i in range(start, start+availabe+1):
                cur.append(i)
                backtrack(i+1, cur)
                cur.pop()

        backtrack(1, [])
        return ans