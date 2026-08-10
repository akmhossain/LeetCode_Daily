class Robot:
    # it is an invariant that the robot will always stay on the permiter of the grid
    # map out every step on the perimeter, with facing directions for each
    def __init__(self, width: int, height: int):
        self.moved = False # for edge case when robot faces south at 0,0 after 1 iteration
        self.idx = 0 # current index on the perimeter
        self.pos = []
        self.dir = []

        for i in range(width): # bottom edge
            self.pos.append((i,0))
            self.dir.append("East")
        for i in range(1, height): # right edge
            self.pos.append((width-1, i))
            self.dir.append("North")
        for i in range(width-2,-1,-1): # top edge
            self.pos.append((i,height-1))
            self.dir.append("West")
        for i in range(height-2, 0, -1): # left edge top exclusive
            self.pos.append((0, i))
            self.dir.append("South")
        self.dir[0] = "South"

    def step(self, num: int) -> None:
        self.moved = True
        self.idx = (self.idx + num) % len(self.pos) # wrap around

    def getPos(self) -> List[int]:
        return self.pos[self.idx]

    def getDir(self) -> str:
        if not self.moved:
            return "East" 
        return self.dir[self.idx]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()