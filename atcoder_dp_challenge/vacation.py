def main():
    n = int(input())
    dp = list(map(int, input().split()))
    for _ in range(n - 1):
        one_day = list(map(int, input().split()))
        one_day[0] += max(dp[1], dp[2])
        one_day[1] += max(dp[0], dp[2])
        one_day[2] += max(dp[0], dp[1])
        dp = one_day
    return max(dp)
print(main())
