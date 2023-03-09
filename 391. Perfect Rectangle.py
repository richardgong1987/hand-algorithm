from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # Calculate the bounding box of all rectangles
        x1, y1, x2, y2 = float('inf'), float('inf'), float('-inf'), float('-inf')
        area = 0
        points = set()
        for rect in rectangles:
            x1 = min(x1, rect[0])
            y1 = min(y1, rect[1])
            x2 = max(x2, rect[2])
            y2 = max(y2, rect[3])
            area += (rect[2] - rect[0]) * (rect[3] - rect[1])
            # Add rectangle vertices to set of points
            for point in [(rect[0], rect[1]), (rect[0], rect[3]), (rect[2], rect[1]), (rect[2], rect[3])]:
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)
        # Check that bounding box area equals sum of rectangle areas
        if area != (x2 - x1) * (y2 - y1):
            return False
        # Check that there are only four vertices
        if len(points) != 4:
            return False
        # Check that all vertices except for corners appear an even number of times
        corners = {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
        for point in points:
            if point not in corners:
                return False
        return True
