from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        div = len(arr)//4+1
        for i in range(len(arr)-div+1):
            if arr[i] == arr[i+div-1]:
                return arr[i]