class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #just find the min sub-array sum of length (len(cardpoint)-k) then return the difference from the total sum
        window, rst = 0, 0
        k = len(cardPoints)-k
        total_sum = 0

        for i in range(len(cardPoints)):
            if i>=k:
                window += (cardPoints[i]-cardPoints[i-k]) 
                rst = min(rst, window) 
            else:
                window += cardPoints[i]
                rst = window
            total_sum += cardPoints[i]

        return total_sum-rst