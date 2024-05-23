h, w = map(int, input().split())
path = []
for _ in range(h):
    path.append(input())

dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if path[i][j] == '#': continue
        dp[i][j] += dp[i-1][j] if i > 0 and path[i-1][j] == "." else 0
        dp[i][j] += dp[i][j-1] if j > 0 and path[i][j-1] == "." else 0
mod = 10**9 + 7
print(dp[h-1][w-1] % mod)
