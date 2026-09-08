class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0


        l, r = 0, len(height)-1
        res = 0
        maxL, maxR = height[l], height[r]

        while l < r:
            # if left is small increment L
            # count water captured
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL-height[l]
            
            # if right is small decrement R
            # count water captured
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]


        return res

        