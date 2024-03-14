class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)-1
        low, high = 0, n

        if target >= letters[n] or target < letters[0]: 
            return  letters[0] 

        while low < high:
            mid = (low+high)//2
            if letters[mid] > target:
                high = mid
            else:
                low = mid + 1 
        return letters[low]