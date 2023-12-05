class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good_int = ""
        for i in range(len(num)-2):
            if int(num[i:i+3]) % 111 == 0:
                max_good_int = max(max_good_int, num[i:i+3])
        
        return max_good_int
        