class Warehouse(object):


    def __init__(self, y, x):
        self.grid = [0] * y
        for i in range(y):
            self.grid[i] = [0]*x
        self.x = x
        self.y = y
    
    def _boundary(self, y, x):
        if(y >= self.y or y < 0 or x >= self.x or x < 0):
            print("Out of bounds!")
            return False
        return True

    def addRobot(self, y, x):
        if(self._boundary(y,x)):
            self.grid[y][x] = 1
            print("Robot added")
            return True
        print("Robot not added")
        return False

    def removeRobot(self, y, x):
        if(self.grid[y][x] == 0 or not(self._boundary(y,x))):
            print("No robot to remove!")
            return False
        self.grid[y][x] = 0
        print("Robot removed")
        return True

    def moveRobot(self, pos1, pos2):
        y1 = pos1[0]
        x1 = pos1[1]
        y2 = pos2[0]
        x2 = pos2[1]
        if(self.grid[y1][x1] == 0 or not(self._boundary(y1,x1))):
            print("No robot to move!")
            return False
        elif(not(self._boundary(y2,x2))):
            print("Robot will hit the wall, it did not move")
            return False
        elif(self.grid[y2][x2] == 1):
            print("Robbot already there!")
            return False

        self.grid[y1][x1] = 0
        self.grid[y2][x2] = 1
        print("Robot moved")
        return True

    def showWarehouse(self):
        for i in range(self.y):
            print(self.grid[i])
        
'''
wh = Warehouse(3,2)
wh.showWarehouse()
wh.addRobot(1,1)
wh.addRobot(2,1)
wh.showWarehouse()

wh.moveRobot(-1,1, 0,0)
wh.showWarehouse()


Wharehouse(3,3):

x0  [0][0]  [0][1] [0][2]
x1  [1][0]  [1][1] [1][2] 
x2  [2][0]  [2][1] [2][2]
    y0      y1     y2
'''