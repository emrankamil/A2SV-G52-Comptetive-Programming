class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters)-1
        while low < high:
            mid = (low+high)//2
            if letters[mid] > target:
                high = mid
            else:
                low = mid + 1 
        if letters[low] > target:
            return letters[low]
        return letters[0]