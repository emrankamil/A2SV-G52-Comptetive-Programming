# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def sorting_fun(num):
            if not num: return mapping[num]
            rst = []
            fac = 10
            while num:
                mapp = mapping[num%fac]
                rst.append(str(mapp))
                num //= 10
            rst.reverse()
            if rst:
                return int("".join(rst))
            return 0
     
        nums.sort(key=sorting_fun)
        return nums