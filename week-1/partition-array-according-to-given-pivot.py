class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greaterThanPivot = []
        lessThanPivot = []
        countPivot = 0

        for num in nums:
            if num < pivot:
                lessThanPivot.append(num)
            elif num > pivot:
                greaterThanPivot.append(num)
            else:
                countPivot += 1

        return lessThanPivot + [pivot]*countPivot + greaterThanPivot

        