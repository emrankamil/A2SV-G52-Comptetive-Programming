class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = [0]*len(arr2)
        arr = []
        for i in arr1:
            if i in arr2:
                counter[arr2.index(i)] += 1
            else:
                arr.append(i)
        rst = []
        for i in range(len(counter)):
            rst.extend([arr2[i]]*counter[i])
        return rst+sorted(arr)