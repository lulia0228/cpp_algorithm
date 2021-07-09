class Solution:
    def __init__(self, *args, **kwargs):
        self.m = 0
        self.n = 0
        self.oris = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        visited = [[False] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                # if board[i][j] == word[0]:
                if self.dfs(word, board, i, j, visited, 0):
                    return True
        return False

    def dfs(self, word, board, x, y, visited, idx):
        if idx == len(word) - 1:
            return word[idx] == board[x][y]
        if board[x][y] == word[idx]:
            visited[x][y] = True
            for ori in self.oris:
                new_x = x + ori[0]
                new_y = y + ori[1]
                if 0 <= new_x < self.m and 0 <= new_y < self.n and not visited[new_x][new_y]:
                    if self.dfs(word, board, new_x, new_y, visited, idx + 1):
                        return True
            visited[x][y] = False
        return False


