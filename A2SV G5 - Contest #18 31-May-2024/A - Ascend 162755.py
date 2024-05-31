# Problem: A - Ascend - https://codeforces.com/gym/526229/problem/A

n = int(input())
l = list(map(int, input().split()))
rst = 1
cur = 1
for i in range(1, n):
    if l[i] > l[i-1]:
        cur += 1
    else:
        rst = max(rst, cur)
        cur = 1
print(max(rst, cur))