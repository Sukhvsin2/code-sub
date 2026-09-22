class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1 # start 0 index and end len(nums)-1 index

        while l <= r:
            mid = (l+r) // 2 # find mid

            if nums[mid] < target: # if target is bigger than mid value
                l = mid + 1 # move left pointer to mid + 1

            elif nums[mid] > target: # else if target is smaller than mid value
                r = mid - 1 # move right to mid - 1
            elif nums[mid] == target: # found the target
                return mid # return index

        # default case if target is not found
        return -1
