import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))

    dp = [0] * n
    for i in range(n-2, -1, -1):
        ans = float('inf')
        for j in range(1, k+1):
            if i+j >= n: 
                break
            ans = min(ans, dp[i+j] + abs(l[i] - l[i+j]))
        dp[i] = ans
    print(dp[0])

if __name__ == "__main__":
    main()
