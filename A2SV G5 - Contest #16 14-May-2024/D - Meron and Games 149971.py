# Problem: D - Meron and Games - https://codeforces.com/gym/523525/problem/D


from collections import Counter, defaultdict
import sys, threading
 
def main():
    n = int(input())
    l = list(map(int, input().split()))
    c = Counter(l)
    lst = list(set(l))
    lst.sort()

    memo = defaultdict(int)
    def dp(i):
        if i >= len(lst):
            return 0
        if i not in memo:
            rst = 0
            if i < len(lst)-1 and lst[i+1] == lst[i]+1:
                pick = lst[i] * c[lst[i]] + dp(i+2)
            else:
                pick = lst[i] * c[lst[i]] + dp(i+1)
            rst = max(pick , dp(i+1))
            memo[i] = rst
        return memo[i]

    print(dp(0))
 
    
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
 
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
