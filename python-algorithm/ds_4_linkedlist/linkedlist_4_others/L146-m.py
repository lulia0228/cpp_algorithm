#--coding:utf-8--
'''
@Time   : 2020/8/14
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.pre = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到末尾，所以定义一个方法
    def move_node_to_head(self, key):
            node = self.hashmap[key]
            # if node.pre and node.next:
            node.pre.next = node.next
            node.next.pre = node.pre
            # 之后将node插入到首节点之后
            node.next = self.head.next
            node.pre = self.head
            self.head.next.pre = node
            self.head.next = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果已经在链表中了就把它移到首端/末尾（变成最新访问的）；2个位置都可以作为最新访问的
            self.move_node_to_head(key)
        res = self.hashmap.get(key, -1) # python字典的特性，可以设定key不存在时候的返回值-1
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的value
            self.hashmap[key].value = value
            # 之后将该节点移到首端
            self.move_node_to_head(key)
        else:
            # 如果不在哈希表中的话就直接插入到头节点后
            if len(self.hashmap) == self.capacity:
                # 去掉哈希表对应项
                self.hashmap.pop(self.tail.pre.key)
                # 去掉最久没有被访问过的节点，即尾节点之前的节点
                self.tail.pre = self.tail.pre.pre
                self.tail.pre.next = self.tail
            new_node = ListNode(key, value)
            self.hashmap[key] = new_node
            # 插入到头节点之后
            new_node.next = self.head.next
            new_node.pre = self.head
            self.head.next.pre = new_node
            self.head.next = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)