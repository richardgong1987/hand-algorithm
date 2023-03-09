from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        ys = set()
        for rect in rectangles:
            ys.add(rect[1])
            ys.add(rect[3])
        ys = sorted(list(ys))

        def getWidth(xs):
            w = 0
            xs.sort()

            start, end = xs[0]
            for a, b in xs:
                if a > end:
                    w += end - start
                    start = a
                end = max(end, b)
            w += end - start
            return w

        result = 0
        for i, y in enumerate(ys[:-1]):
            xs = []

            for x1, y1, x2, y2 in rectangles:
                if y1 <= y < y2:
                    xs.append([x1, x2])
            if xs:
                withs = getWidth(xs)
                result += withs * (ys[i + 1] - y)

        return result % (10 ** 9 + 7)


# 0 2
# y=0, xs=[[0, 2], [1, 2], [1, 3]]
# 0 2
# y=1, xs=[[0, 2], [1, 2]]
# 1 2
# y=2, xs=[[1, 2]]

solution = Solution()
print(solution.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))
