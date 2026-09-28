class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # taking default first element smallest

        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2

            res = min(nums[mid], res) # if the mid has a smaller value
                
            # find the smaller sorted arr
            if nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1

        return res