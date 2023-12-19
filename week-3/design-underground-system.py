class UndergroundSystem:

    def __init__(self):
        self.checkin=defaultdict(tuple)
        self.checkout=defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id]=(t,stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        starttime,startstation=self.checkin[id]
        total=t-starttime
        self.checkout[(startstation,stationName)].append(total)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.checkout[(startStation,endStation)])/len(self.checkout[(startStation,endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)