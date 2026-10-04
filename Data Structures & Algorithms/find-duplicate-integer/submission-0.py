class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        s2 = 0
        while s2 != slow:
            slow = nums[slow]
            s2 = nums[s2]

        return s2