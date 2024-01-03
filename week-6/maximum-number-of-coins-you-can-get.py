class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        rst = 0
        piles.sort()
        i = len(piles)//3
        while i < len(piles):
            rst += piles[i]
            i += 2

        return rst
        