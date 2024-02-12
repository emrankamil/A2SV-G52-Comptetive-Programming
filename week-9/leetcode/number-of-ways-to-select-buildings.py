class Solution:
    def numberOfWays(self, s: str) -> int:
        rst = 0
        counter = {0:[0,0],1:[0,0]}

        for i in s:
            cur = int(i)
            counter[cur][0] += 1
            if counter[(cur+1)%2][0]!= 0:
                rst += counter[(cur+1)%2][1]
                counter[cur][1] += counter[(cur+1)%2][0]
        return rst

# zero_counter = [0, 0]
# one_counter = [0, 0]
# if s[i] == "0":
#     zero_counter[0] += 1
#     if one_counter[0] != 0:
#         rst += one_counter[1]
#         zero_counter[1] += one_counter[0]
    
# elif s[i] == "1":
#     one_counter[0] += 1
#     if zero_counter[0] != 0:
#         rst += zero_counter[1]
#         one_counter[1] += zero_counter[0]