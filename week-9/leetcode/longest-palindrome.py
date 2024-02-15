class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        check = False
        rst = 0
        for i in count:
            if count[i]%2==0:
                rst += count[i]
            else:
                check = True
                rst += count[i]-1
        return rst+check
