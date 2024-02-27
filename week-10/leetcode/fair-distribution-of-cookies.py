class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if len(cookies)==k:
            return max(cookies)

        average = sum(cookies)/k
        rst = float('inf')
        distribs = [0]*k

        def backtrack(start,cur):
            nonlocal rst
            if cur == len(cookies): 
                rst = min(rst, max(distribs))
                return
            for i in range(start, k):
                if cookies[cur] >= average:
                    distribs[i] += cookies[cur]
                    backtrack(start+1, cur+1)
                elif cur<(len(cookies)-distribs.count(0)):
                    distribs[i] += cookies[cur]
                    backtrack(start, cur+1)
                    distribs[i] -= cookies[cur]

        cookies.sort(reverse=True)
        backtrack(0,0)
        return rst
