# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        next_greater = [0]*n
        cur_greater = height[-1]
        for i in range(n-2, -1, -1):
            if height[i] <= cur_greater:
                next_greater[i] = cur_greater
            else:
                cur_greater = height[i]

        result = 0
        left_wall = 0
        for i in range(n):
            if height[i] < left_wall:
                right_wall = next_greater[i]
                border = min(left_wall, right_wall)

                if border > height[i]:
                    result += border - height[i]
            else:
                left_wall = height[i]

        return result