# Recursion 응용 - 미로찾기
class Maze:
    def __init__(self):
        self.N = 8
        self.maze = [[0, 0, 0, 0, 0, 0, 0, 1],
                     [0, 1, 1, 0, 1, 1, 0, 1],
                     [0, 0, 0, 0, 0, 0, 0, 1],
                     [0, 1, 0, 0, 1, 1, 0, 0],
                     [0, 1, 1, 1, 0, 0, 1, 1],
                     [0, 1, 0, 0, 0, 1, 0, 1],
                     [0, 0, 0, 1, 0, 0, 0, 1],
                     [0, 1, 1, 1, 0, 1, 0, 0]]
        
        self.PATHWAY_COLOR = 0 # 갈수 있는 길
        self.WALL_COLOR = 1 # 갈수 없는 길
        self.BLOCKED_COLOR = 2 # Visited 이며 출구까지의 경로상에 있지 않음이 밝혀진 Cell
        self.PATH_COLOR = 3 # Visisted 이며 아직 출구로 가는 경로가 될 가능성이 있는 Cell

    def findMazePath(self, x, y):
        if (x < 0 or y < 0 | x >= N or y >= N): # Map 에 속하지 않는 범위
            return False

        elif (self.maze[x][y] != self.PATHWAY_COLOR): # 갈 수 없는 길 확인
            return False

        elif (x == self.N - 1 & y == self.N - 1):
            self.maze[x][y] = self.PATH_COLOR # 최종 목적지가 Path_color 이면 경로 존재
            return True

        else:
            self.maze[x][y] = self.PATH_COLOR # 갈 수 있는 길 확인
            if (self.findMazePath(x - 1, y) | self.findMazePath(x, y + 1) | \
                self.findMazePath(x + 1, y) | self.findMazePath(x, y - 1)):
                return True
            self.maze[x][y] = self.BLOCKED_COLOR # 갈 수 없는 길 표시
            return False

if __name__ == '__main__':
    s = Maze()
    print(s.maze)
    s.findMazePath(0, 0)
    print(s.maze)
