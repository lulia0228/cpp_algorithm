#--coding:utf-8--

'''如果两个矩形重叠，那么它们重叠的区域一定也是一个矩形，
那么这代表了两个矩形与 x 轴平行的边（水平边）投影到 x 轴上时会有交集，
与 y 轴平行的边（竖直边）投影到 yy轴上时也会有交集。
因此，我们可以将问题看作一维线段是否有交集的问题。'''

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)

        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))

