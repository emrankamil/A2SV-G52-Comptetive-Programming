class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        total = answers[0]+1
        last_count = 1
        for i in range(1,len(answers)):
            if answers[i]!=answers[i-1] or answers[i]-last_count+1 == 0:
                total += (answers[i]+1)
                last_count = 1
            else:
                last_count += 1
        return total