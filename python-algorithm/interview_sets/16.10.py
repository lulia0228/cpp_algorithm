#--coding:utf-8--
class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        # 前缀和的思想
        lives, ghosts = [0] * 101, [0] * 101
        for i in birth:
            lives[i - 1900] += 1
        for j in death:
            ghosts[j - 1900] += 1

        for i in range(1, 101):
            lives[i] = lives[i - 1] + lives[i]
        for j in range(1, 101):
            ghosts[j] = ghosts[j - 1] + ghosts[j]

        res, year = lives[0], 0
        for i in range(1, 101):
            tmp = lives[i] - ghosts[i - 1]
            if tmp > res:
                res = tmp
                year = i

        return 1900 + year