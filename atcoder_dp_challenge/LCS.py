s = input()
t = input()
n, m = len(s), len(t)
dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 1
        else: 
            if i > 0: dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j > 0: dp[i][j] = max(dp[i][j], dp[i][j-1])

i, j = n - 1, m - 1
common = []
while i >= 0 and j >= 0:
    if s[i] == t[j]:
        common.append(s[i])
        i, j = i -1, j -1
    else:
        if i > 0 and dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1]:
            j -= 1
        else: break
print("".join(common[::-1]))
