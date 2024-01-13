class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_count, f_count = 0, 0
        rst, count, left = 0, 0, 0

        for i in range(len(answerKey)):
            if answerKey[i] == "T":
                t_count += 1
            else:
                f_count += 1
            
            if min(t_count, f_count) <= k:
                if i+1 == len(answerKey):
                    rst = max(rst, count+1)
                count += 1
            else:
                rst = max(rst, count)
                if answerKey[left] == "T":
                    t_count -= 1
                else:
                    f_count -= 1
                left += 1
        return rst
