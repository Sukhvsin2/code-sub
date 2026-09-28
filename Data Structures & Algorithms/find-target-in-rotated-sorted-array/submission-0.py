class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        res = -1
        
        # binary search on rotated sorted arr
        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target: # found the target
                return mid # return index


            # find which arr left or right has the target
            
            # means arr is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]: # target b/w range since sorted arr
                    r = mid - 1
                else:
                    l = mid + 1

            else: # arr not sorted order
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return res