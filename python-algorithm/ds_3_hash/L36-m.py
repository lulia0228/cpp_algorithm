# -*- coding: utf-8 -*-


# 36. 有效的数独

# (i,j)属于某个宫格的计算公式为 : j//3 + (i//3) * 3
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 分别记录每行、每列、每个格内部是否出现数字1~9
        row = [[0 for i in range(10)] for i in range(9)]
        col = [[0 for i in range(10)] for i in range(9)]
        box = [[0 for i in range(10)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                cur_num = int(board[i][j])
                # 判断是否出现过
                if row[i][cur_num] == 1:
                    return False
                if col[j][cur_num] == 1:
                    return False
                if box[j // 3 + (i // 3) * 3][cur_num] == 1:
                    return False
                row[i][cur_num] = 1
                col[j][cur_num] = 1
                box[j // 3 + (i // 3) * 3][cur_num] = 1
        return True
