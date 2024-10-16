# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        def check_pos(diff, balls):
            start = position[0]
            for i in range(1, len(position)):
                if position[i] - start >= diff:
                    balls -= 1
                    if balls == 1:
                        return True
                    start = position[i]
            return balls == 1


        position.sort()
        low, high = 1, position[-1] - position[0]
        while low < high:
            mid = (low + high + 1)//2
            if check_pos(mid, m):
                low = mid
            else:
                high = mid - 1
        return low