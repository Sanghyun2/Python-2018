# 초기 값 설정
block = [[1, 0, 0, 0, 0, 0, 0, 1],
         [0, 1, 1, 0, 0, 1, 0, 0],
         [1, 1, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 1, 0, 0],
         [1, 0, 0, 0, 1, 0, 0, 1],
         [0, 1, 1, 0, 0, 1, 1, 1]]

N = len(block[0])   # 정사각행렬의 행의 개수(열의 개수) 계산
BackgroundColor = 0 # Counting 하지 않아도 되는 공간
ImageColor = 1      # Counting 해야하는 공간
AlreadyCounted = 2  # 이미 Counting 이루어진 공간

# Cell 의 개수를 counting 해주는 function = CountCells(A,x,y)
def CountCells(A,x,y):
    if (x < 0 or y < 0 | x >= N or y >= N): # 범위를 벗어난 경우
        return 0

    elif A[x][y] != ImageColor: # Counting 해야하는 공간이 아닌 경우
        return 0

    else:
        A[x][y] = 2
        return 1 + CountCells(A,x-1,y+1) + CountCells(A,x,y+1) + CountCells(A,x+1,y+1) + CountCells(A,x-1,y) + CountCells(A,x+1,y) + CountCells(A,x-1,y-1) + CountCells(A,x,y-1) + CountCells(A,x+1,y-1)

CountCells(block,3,5)
