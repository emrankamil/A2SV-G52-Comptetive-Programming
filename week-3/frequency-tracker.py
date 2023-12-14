from collections import Counter
class FrequencyTracker:

    def __init__(self):
        self.array = Counter()
        self.freqContainer = Counter() #key: frequency, value:count of numbeers with that frequncy
        

    def add(self, number: int) -> None:
        if self.freqContainer[self.array[number]] > 0:
            self.freqContainer[self.array[number]] -= 1
        self.array[number]+= 1
        self.freqContainer[self.array[number]] += 1

    def deleteOne(self, number: int) -> None:
         if number in self.array:
            if self.freqContainer[self.array[number]] > 0:
                self.freqContainer[self.array[number]] -= 1
            self.array[number] -= 1
            if self.array[number]<=0:
                del self.array[number]
            self.freqContainer[self.array[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqContainer[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

   