class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort it
        nums = sorted(nums)
        result = []

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue

            l = k+1
            r = len(nums)-1

            while l < r:
                threeSum = nums[k] + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    result.append([nums[l], nums[r], nums[k]])
                    l += 1
                    r -= 1

                    # if found a match check left dups
                    while nums[l] == nums[l-1] and l < r:
                        l += 1


        return result