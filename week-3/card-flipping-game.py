class Solution:
    def flipgame(self, fronts, backs):
        
        s = set()
        res = float('inf')
        for f, b in zip(fronts, backs):
            if f == b:
                s.add(f)
        for f in fronts:
            if f not in s:
                res = min(res, f)
        for b in backs:
            if b not in s:
                res = min(res, b)
        return 0 if res == float('inf') else res