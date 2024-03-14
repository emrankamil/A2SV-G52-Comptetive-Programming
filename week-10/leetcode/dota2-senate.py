class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        cur = deque(senate)
        r, d = senate.count('R'), senate.count('D')
        removed_r, removed_d = 0, 0
        while cur:
            if r == 0: return "Dire"
            if d == 0: return 'Radiant'
            if cur[0] == 'D':
                if removed_d:
                    cur.popleft()
                    removed_d -= 1
                else:
                    cur.append(cur.popleft())
                    removed_r += 1
                    r -= 1
            if cur[0] == 'R':
                if removed_r:
                    cur.popleft()
                    removed_r -= 1
                else:
                    cur.append(cur.popleft())
                    removed_d += 1
                    d -= 1
                
            