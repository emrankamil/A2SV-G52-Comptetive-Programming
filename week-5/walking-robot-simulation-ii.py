class Robot:

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.perimeter = 2*(width+height-2)
        self.dir = "East"
        self.pos = [0,0]

    def step(self, num: int) -> None:
        num %= self.perimeter
        if num == 0 and self.pos == [0,0]:
            self.dir = "South"
            
        while num:
            if self.dir == "East":
                distance = self.width-1-self.pos[0]
                if num > distance:
                    num -= distance
                    self.dir = "North"
                    self.pos[0] = self.width-1
                else:
                    self.pos[0] += num
                    num = 0
            elif self.dir == "North":
                distance = self.height-1-self.pos[1]
                if num > distance:
                    num -= distance
                    self.dir = "West"
                    self.pos[1] = self.height-1
                else:
                    self.pos[1] += num
                    num = 0
            elif self.dir == "West":
                distance = self.pos[0]
                if num > distance:
                    num -= distance
                    self.dir = "South"
                    self.pos[0] = 0
                else:
                    self.pos[0] -= num
                    num = 0
            elif self.dir == "South":
                distance = self.pos[1]
                if num > distance:
                    num -= distance
                    self.dir = "East"
                    self.pos[1] = 0
                else:
                    self.pos[1] -= num
                    num = 0


    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir   


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()