class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0


        l, r = 0, len(height)-1
        res = 0
        maxL, maxR = height[l], height[r]

        while l < r:
            # print("maxL: ", maxL)
            # print("maxR: ", maxR)

            # if left is small increment L
            # count water captured
            if maxL < maxR:
                # print("l moved++")
                l += 1
                # print("l position: ", l)
                # print(f"{maxL} - {height[l]} = ", maxL - height[l])
                maxL = max(maxL, height[l])
                res += maxL-height[l]
                # print("res is now: ", res)
                # else:
                    # print("can't trap water because", maxL - height[l])
            
            # if right is small decrement R
            # count water captured
            else:
                # print("r moved--")
                r -= 1
                # print("r position: ", r)
                # print(f"{maxR} - {height[r]} = ", maxR - height[r])
                maxR = max(maxR, height[r])
                res += maxR - height[r]
                # print("res is now: ", res)
                # else:
                    # print("can't trap water because", maxR - height[r])


        return res

        