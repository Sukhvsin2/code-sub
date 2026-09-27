class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = nums[0]
        prev = nums[0]
        for n in nums:
            if n < prev:
                m = min(prev, n)
            prev = n

        return m