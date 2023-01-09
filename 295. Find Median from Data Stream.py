from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)
        heappush(self.min_heap, -heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) != len(self.max_heap):
            return -self.max_heap[0]

        return (self.min_heap[0] + (-self.max_heap[0])) / 2


finder = MedianFinder()
A = [2, 1, 5, 7, 2, 0, 5]
for _, num in enumerate(A):
    finder.addNum(num)
    print(finder.findMedian())
