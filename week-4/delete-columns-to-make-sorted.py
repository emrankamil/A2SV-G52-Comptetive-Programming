class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        counter = 0
        for i in range(m):
            for j in range(1,n):
                if strs[j][i] < strs[j-1][i]:
                    counter += 1
                    break
        return counter

        