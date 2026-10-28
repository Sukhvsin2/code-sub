class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        if not self.arr: return float(0)
        
        self.arr.sort()

        if len(self.arr) == 1: return self.arr[0]

        if len(self.arr) % 2 == 0: # even list
            r = len(self.arr) // 2
            l = r - 1
            return (self.arr[l] + self.arr[r]) / 2
        else:
            return self.arr[len(self.arr) // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()