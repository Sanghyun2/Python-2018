# Cell 의 개수를 counting 해주는 function
class cell:
    def __init__(self):
        self.N = 8
        self.BackgroundColor = 0 # Counting 하지 않아도 되는 공간
        self.ImageColor = 1      # Counting 해야하는 공간
        self.AlreadyCounted = 2  # 이미 Counting 이루어진 공간
        self.block = [[1, 0, 0, 0, 0, 0, 0, 1],
                      [0, 1, 1, 0, 0, 1, 0, 0],
                      [1, 1, 0, 0, 1, 0, 1, 0],
                      [0, 0, 0, 0, 0, 1, 0, 0],
                      [0, 1, 0, 1, 0, 1, 0, 0],
                      [0, 1, 0, 1, 0, 1, 0, 0],
                      [1, 0, 0, 0, 1, 0, 0, 1],
                      [0, 1, 1, 0, 0, 1, 1, 1]]
    
    def CountCells(self,x,y):
        if (x < 0 or y < 0 | x >= self.N or y >= self.N): # 범위를 벗어난 경우
            return 0
        
        elif self.block[x][y] != self.ImageColor: # Counting 해야하는 공간이 아닌 경우
            return 0
        
        else:
            self.block[x][y] = 2
            return 1 + self.CountCells(x-1,y+1) + self.CountCells(x,y+1) + self.CountCells(x+1,y+1) + self.CountCells(x-1,y) + self.CountCells(x+1,y) + self.CountCells(x-1,y-1) + self.CountCells(x,y-1) + self.CountCells(x+1,y-1)

if __name__ == '__main__':
    C = cell()
    print(C.block)
    print(C.CountCells(3,5))
    print(C.block)
