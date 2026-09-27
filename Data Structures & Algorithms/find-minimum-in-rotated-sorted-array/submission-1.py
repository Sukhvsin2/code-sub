class Solution:
    def findMin(self, nums: List[int]) -> int:

        # complexity 
        # time: O(n) - worst if we have a sorted list [1,2,3..,N] 
        # have to look for every item

        # space O(1) since, not using additional space.
        
        m = nums[0]
        prev = nums[0]
        for n in nums:
            if n < prev:
                m = min(prev, n)
            prev = n

        return m