class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = {"B": 0, "W": 0}
        
        for i in range(k-1):
            window[blocks[i]] += 1

        rst = k
        for i in range(k-1, len(blocks)):
            window[blocks[i]] += 1
            rst = min(rst, window["W"])
            window[blocks[i - k+1]] -= 1

        return rst