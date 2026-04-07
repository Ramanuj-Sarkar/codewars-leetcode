# the robot is in a [width, height] playfield
# it starts at [0, 0] facing east
# it goes around the perimeter with step()
class Robot:

    def __init__(self, width: int, height: int):
        self.maxes = [width, height]

        self.pos = [0, 0]
        self.dir = 0  # corresponds to east

        # steps to take around the perimeter
        self.perimeter = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        if self.perimeter == 0:
            return

        num %= self.perimeter

        # this is what happens if a full cycle occurs
        if num == 0:
            if self.pos == [0, 0]:
                self.dir = 3  # South
            return


        for _ in range(num):
            # horizontal or vertical?
            ne = self.dir % 2

            # positive or negative change?
            ns = -1 if self.dir // 2 == 1 else 1

            newpos = self.pos[ne] + ns
                
            if not 0 <= newpos < self.maxes[ne]:
                self.dir = (self.dir + 1) % 4

                # horizontal or vertical?
                ne = self.dir % 2

                # positive or negative change?
                ns = -1 if self.dir // 2 == 1 else 1

                newpos = self.pos[ne] + ns
            
            self.pos[ne] = newpos

        

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return ["East", "North", "West", "South"][self.dir]
