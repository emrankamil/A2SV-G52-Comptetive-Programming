class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        rst  = []
        if n < (k+(k*(k-1))//2): return [] # if n is less than the least possible sum using k numbers

        def backtrack(start, cur, cur_sum):
            if cur_sum > n:
                return
            if len(cur) == k:
                if cur_sum == n:
                    rst.append(cur[:])
                else: return

            for i in range(start, 10):
                cur.append(i)
                cur_sum += i

                backtrack(i+1, cur, cur_sum)

                cur.pop()
                cur_sum -= i

        backtrack(1, [], 0)
        return rst