class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bitset = ["0"]*size   
        self.bitsetSum = 0   
        self.rule = ["0", "1"]

    def fix(self, idx: int) -> None:
        if self.bitset[idx] == self.rule[0]:
            self.bitset[idx] = self.rule[1]
            self.bitsetSum += 1
        
    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == self.rule[1]:
            self.bitset[idx] = self.rule[0]
            self.bitsetSum -= 1

    def flip(self) -> None:
        # for i in range(self.size):
        #     self.bitset[i] = int(not self.bitset[i])
        self.bitsetSum = self.size - self.bitsetSum
        self.rule[0], self.rule[1] = self.rule[1], self.rule[0]

    def all(self) -> bool:
        return self.bitsetSum == self.size

    def one(self) -> bool:
        return self.bitsetSum != 0   

    def count(self) -> int:
        return self.bitsetSum    

    def toString(self) -> str:
        if self.rule == ["0", "1"]:
            return ''.join(i for i in self.bitset )
        else:
            return ''.join("1" if i=="0" else "0" for i in self.bitset)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()