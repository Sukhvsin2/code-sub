class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # range 1 - max pile of bananas
        res = r # since koko can eat max bananas under h hours
        while l <= r:
            mid = (l+r) // 2
            totalHours = 0
            for p in piles:
                totalHours += math.ceil(p/mid)

            if totalHours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res