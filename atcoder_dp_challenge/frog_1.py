n = int(input())
l = list(map(int, input().split()))

dp = [0] * n
dp[n-2] = abs(l[n-2]-l[n-1])
for i in range(n-3, -1, -1):
    dp[i] = min(dp[i+1] + abs(l[i] - l[i+1]), dp[i+2] + abs(l[i] - l[i+2]))
print(dp[0])
