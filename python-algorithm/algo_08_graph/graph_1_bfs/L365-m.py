#--coding:utf-8--

# 水壶倒腾水问题

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        queue = [(0, 0)]
        seen = set((0, 0))

        while(len(queue) > 0):
            a, b = queue.pop(0)
            if a ==z or b == z or a + b == z:
                return True
            states = set()

            # 每次共6种操作
            states.add((x, b)) # 倒满第一个
            states.add((a, y)) # 倒满第二个
            states.add((0, b)) # 清空第一个
            states.add((a, 0)) # 清空第二个
            states.add((min(x, b + a), 0 if b < x - a else b - (x - a))) # 第二个往第一个倒水
            states.add((0 if a + b < y else a - (y - b), min(b + a, y))) # 第一个往第二个倒水
            for state in states:
                if state in seen:
                    continue;
                queue.append(state)
                seen.add(state)
        return False

# 数学

# 定理：
# 对任意两个整数 a、b，设 d是它们的最大公约数。那么关于未知数x和y的线性方程（称为裴蜀等式）：
# ax+by=m 有整数解  (x,y) 当且仅当m是d的整数倍。裴蜀等式有解时必然有无穷多个解。

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False

        if (z == 0):
            return True

        if (x == 0):
            return y == z

        if (y == 0):
            return x == z

        def GCD(a, b):
            smaller = min(a, b)
            while smaller:
                if a % smaller == 0 and b % smaller == 0:
                    return smaller
                smaller -= 1

        return z % GCD(x, y) == 0

