class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix = [0]*len(customers)
        total_y = 0
        for i in range(len(customers)):
            if customers[i] == "Y":
                prefix[i] = prefix[i-1]+1
                total_y += 1
            else:
                prefix[i] = prefix[i-1]
        

        penalty = total_y
        rst = 0
        for i in range(len(prefix)):
            left_N = i-prefix[i]+1
            right_Y = total_y - prefix[i]
            if left_N+right_Y < penalty:
                penalty = left_N+right_Y
                rst = i+1

        return rst
        