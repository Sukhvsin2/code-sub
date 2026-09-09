class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        totalWater = 0

        while l < r:
            if maxL < maxR:
                l+=1
                maxL = max(maxL, height[l])
                totalWater += maxL - height[l]
            else:
                r-=1
                maxR = max(maxR, height[r])
                totalWater += maxR - height[r]
        return totalWater