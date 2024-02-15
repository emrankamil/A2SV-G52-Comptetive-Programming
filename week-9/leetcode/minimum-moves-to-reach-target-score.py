class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        total = 0
        while target > 1:
            if not maxDoubles:
                return total+target-1
            if target%2:
                total += 1
                target -= 1
            else:
                total += 1
                target //= 2
                maxDoubles -= 1
        return total