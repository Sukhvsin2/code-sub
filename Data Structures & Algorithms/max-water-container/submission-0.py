class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        m = 0
        while l < r:
            val = (r-l) * min(heights[l], heights[r])
            m = max(m, val)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        

        return m