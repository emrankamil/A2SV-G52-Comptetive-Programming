class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverse(arr,index):
            for i in range((index+1)//2):
                arr[i], arr[index-i] = arr[index-i], arr[i]

        rst = []
        for i in range(len(arr)-1,0,-1):
            currentMax = max(arr[:i+1])
            indexMax = arr.index(currentMax)
            if indexMax != i:
                if indexMax != 0:
                    reverse(arr, indexMax)
                    rst.append(indexMax+1)
                reverse(arr, i)
                rst.append(i+1)

        return rst
