class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            # once we have the sorted order
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # find sorted order
            mid = (l+r)//2
            res = min(nums[mid], res)

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid-1

        return res