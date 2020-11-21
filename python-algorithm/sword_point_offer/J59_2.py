#--coding:utf-8--


# 可以和最小值栈leetcode155那道题对比

# 另外维护了一个双端队列，并保持其单调

class MaxQueue:

    def __init__(self):
        self.deque = collections.deque()
        self.queue = []

    def max_value(self) -> int:
        if self.queue == []:
            return -1
        return self.deque[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)

    def pop_front(self) -> int:
        if self.queue == []:
            return -1
        tmp = self.queue.pop(0)
        if self.deque[0] == tmp:
            self.deque.popleft()
        return tmp


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()