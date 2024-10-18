# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        def backtrack(orr, start):
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                cur_orr = orr | nums[i]
                counter[cur_orr] += 1
                backtrack(cur_orr, i+1)
                
        backtrack(0, 0)
        max_orr, rst = 0, 0
        for i in counter:
            if i == max_orr:
                rst += counter[i]
            elif i > max_orr:
                max_orr = i
                rst = counter[i]
        return rst