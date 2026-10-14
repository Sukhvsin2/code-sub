# not a good solution
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.largest = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        res = self.nums[-self.largest]
        return res
