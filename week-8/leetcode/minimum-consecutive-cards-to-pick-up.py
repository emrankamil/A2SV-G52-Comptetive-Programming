class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        checked = {}
        left = 0
        rst = float('inf')
        for i in range(len(cards)):
            if cards[i] in checked and checked[cards[i]]>=left:
                rst = min(rst, i-checked[cards[i]]+1)
                left = checked[cards[i]]+1

            checked[cards[i]] = i

        if rst == float('inf'):
            return -1
        else:
            return rst